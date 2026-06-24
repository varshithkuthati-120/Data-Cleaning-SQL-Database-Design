import re
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text

WORKSPACE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = WORKSPACE_DIR / "data" / "mutual_fund.db"
SQL_PATH = WORKSPACE_DIR / "sql" / "analytical_queries.sql"
REPORTS_DIR = WORKSPACE_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def parse_queries(sql_file_path: Path) -> list[tuple[str, str]]:
    with open(sql_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split queries by double-newline followed by a comment indicating a new query
    # E.g., -- 1. , -- 2. , etc.
    raw_blocks = re.split(r"\n+(?=-- \d+\.)", content)
    queries = []
    
    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue
        # Extract the title/description (first few comment lines)
        lines = block.split("\n")
        title_lines = [line.replace("--", "").strip() for line in lines if line.strip().startswith("--")]
        title = " | ".join(title_lines)
        
        # Extract the SQL code (non-comment lines)
        sql_lines = [line for line in lines if not line.strip().startswith("--")]
        sql_code = "\n".join(sql_lines).strip()
        
        if sql_code:
            queries.append((title, sql_code))
            
    return queries


def run_and_report():
    engine = create_engine(f"sqlite:///{DB_PATH}")
    queries = parse_queries(SQL_PATH)
    
    print(f"Loaded {len(queries)} queries from {SQL_PATH}")
    
    report_lines = [
        "# Day 2: Analytical SQL Queries Report",
        "",
        "This report contains the results of running the 10 analytical SQL queries against the SQLite database.",
        ""
    ]
    
    with engine.connect() as conn:
        for idx, (title, sql_code) in enumerate(queries, 1):
            print(f"\nRunning Query {idx}: {title}")
            report_lines.append(f"## Query {idx}: {title}")
            report_lines.append("```sql")
            report_lines.append(sql_code)
            report_lines.append("```")
            report_lines.append("")
            
            try:
                df = pd.read_sql_query(text(sql_code), conn)
                print(f"Result shape: {df.shape}")
                
                # Convert DataFrame to Markdown table
                try:
                    md_table = df.to_markdown(index=False)
                except Exception:
                    # Fallback to simple markdown formatting if tabulate is missing
                    cols = df.columns
                    headers = "| " + " | ".join(map(str, cols)) + " |"
                    align = "| " + " | ".join(["---"] * len(cols)) + " |"
                    rows = []
                    for _, row in df.iterrows():
                        rows.append("| " + " | ".join(map(str, row.values)) + " |")
                    md_table = "\n".join([headers, align] + rows)

                report_lines.append("### Results")
                report_lines.append(md_table)
                report_lines.append("")
                
                # Print first 5 rows to stdout for visibility
                print(df.head(5))
            except Exception as e:
                print(f"Error running query {idx}: {e}")
                report_lines.append(f"### Error\n`{e}`\n")
                
            report_lines.append("---")
            report_lines.append("")
            
    # Save the report
    report_path = REPORTS_DIR / "analytical_queries_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines) + "\n")
        
    print(f"\nSaved query execution report to {report_path}")


if __name__ == "__main__":
    run_and_report()
