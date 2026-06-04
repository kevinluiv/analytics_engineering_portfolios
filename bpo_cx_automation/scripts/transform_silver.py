import duckdb
import os

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "pipeline.db")
BRONZE_MS = os.path.join(BASE_DIR, "data", "bronze", "member_services", "*.csv")
BRONZE_TECH = os.path.join(BASE_DIR, "data", "bronze", "tech_support", "*.csv")

def transformar_a_silver():
    con = duckdb.connect(DB_PATH)
    
    try:
        print("🪄 Iniciando transformación a Capa Silver...")

        # 1. Creamos (o sobrescribimos) la tabla maestra unificada
     # Usamos DISTINCT ON o una subconsulta para evitar duplicados por Conversation ID
        query = f"""
        CREATE OR REPLACE TABLE interactions_silver AS
        SELECT DISTINCT ON ("Conversation ID") * FROM (
            SELECT *, 'Member Services' as business_unit FROM read_csv_auto('{BRONZE_MS}')
            UNION ALL
            SELECT *, 'Tech Support' as business_unit FROM read_csv_auto('{BRONZE_TECH}')
        )
        ORDER BY "Conversation ID", "Survey Score" DESC 
        """
        
        con.execute(query)
        
        # 2. Verificamos el resultado
        count = con.execute("SELECT count(*) FROM interactions_silver").fetchone()[0]
        print(f"✅ ¡Éxito! Tabla 'interactions_silver' creada con {count} registros.")
        
        # Mostrar un resumen por unidad de negocio
        print("\nResumen por Unidad de Negocio:")
        print(con.execute("SELECT business_unit, count(*) FROM interactions_silver GROUP BY 1").df())

    except Exception as e:
        print(f"❌ Error: Asegúrate de tener al menos un archivo CSV en cada carpeta. Detalle: {e}")
    finally:
        con.close()

if __name__ == "__main__":
    transformar_a_silver()