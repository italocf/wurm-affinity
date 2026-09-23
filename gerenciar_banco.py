import sqlite3
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

DB_NAME = "wurm_affinity.db"

def get_conn():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    return sqlite3.connect(os.path.join(dir_path, DB_NAME))

def show_summary():
    conn = get_conn()
    cur = conn.cursor()
    print("\n" + "="*50)
    print("      BANCO DE DADOS WURM AFFINITY (SQLITE)")
    print("="*50)
    
    counts = {}
    for table in ['skills', 'ingredients', 'cookers', 'containers', 'preparations', 'rarities', 'characters', 'saved_recipes']:
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        counts[table] = cur.fetchone()[0]
        print(f" â€¢ Tabela '{table}': {counts[table]} registros")
        
    print("\n--- PERSONAGENS SALVOS ---")
    cur.execute("SELECT id, name, meat_item, veggie_item, player_number, created_at FROM characters")
    chars = cur.fetchall()
    for c in chars:
        print(f" ID #{c[0]}: {c[1]} | Teste: {c[2]} + {c[3]} | Player Number: {c[4]}")
        
    print("\n--- RECEITAS SALVAS NO BANCO ---")
    cur.execute("SELECT r.id, r.name, r.recipe_type, s.name, r.total_affinity_score FROM saved_recipes r JOIN skills s ON r.target_skill_id = s.id")
    recs = cur.fetchall()
    for r in recs:
        print(f" ID #{r[0]}: [{r[2]}] {r[1]} -> Afinidade: {r[3]} (Total: {r[4]})")
    print("="*50 + "\n")
    conn.close()

def query_skill(search_term):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM skills WHERE name LIKE ? ORDER BY name", (f"%{search_term}%",))
    rows = cur.fetchall()
    print(f"\nResultados para '{search_term}':")
    for r in rows:
        print(f" â€¢ ID #{r[0]}: {r[1]}")
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query_skill(sys.argv[1])
    else:
        show_summary()
