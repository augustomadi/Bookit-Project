#!/usr/bin/env python
"""Script simples para executar o linter flake8."""
import subprocess
import sys


def run_linter():
    """Executa o flake8 no projeto."""
    try:
        result = subprocess.run(['flake8', '.'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Linting passou! Nenhum problema encontrado.")
        else:
            print("❌ Problemas de linting encontrados:")
            print(result.stdout)
            print(f"Total de problemas: {len(result.stdout.splitlines())}")
            
    except FileNotFoundError:
        print("❌ Flake8 não encontrado. Execute: pip install flake8")
        sys.exit(1)


if __name__ == '__main__':
    run_linter() 