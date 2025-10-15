#!/usr/bin/env python3
"""Servidor local simples para abrir o site Aurora com um clique.

Executa um HTTP server na porta escolhida e opcionalmente abre o navegador
padrão apontando para index.html.
"""
from __future__ import annotations

import argparse
import contextlib
import http.server
import os
import socket
import socketserver
import sys
import threading
import time
import webbrowser
from pathlib import Path


DEFAULT_PORT = 5500


class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True


def find_free_port(preferred: int) -> int:
    """Retorna a porta disponível mais próxima da preferida."""
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind(("", preferred))
        except OSError:
            sock.bind(("", 0))
        return sock.getsockname()[1]


def run_server(port: int, open_browser: bool) -> None:
    root_dir = Path(__file__).resolve().parent
    os.chdir(root_dir)

    handler_class = http.server.SimpleHTTPRequestHandler
    # Garante que o arquivo de legendas seja servido com o mime-type correto
    handler_class.extensions_map.update({".vtt": "text/vtt"})

    server = ThreadedHTTPServer(("127.0.0.1", port), handler_class)

    url = f"http://127.0.0.1:{port}/index.html"
    print("\n🚀 Servidor local iniciado!")
    print(f"   ➜ Diretório: {root_dir}")
    print(f"   ➜ URL: {url}")
    print("   ➜ Pressione CTRL+C para encerrar.\n")

    if open_browser:
        # Abre o navegador em uma thread separada para não bloquear
        threading.Thread(target=lambda: _open_with_retry(url), daemon=True).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nEncerrando servidor... Até mais! 👋")
    finally:
        server.server_close()


def _open_with_retry(url: str, tentativas: int = 5, atraso: float = 0.5) -> None:
    for tentativa in range(1, tentativas + 1):
        if webbrowser.open(url):
            return
        time.sleep(atraso)
        atraso *= 1.2
    print("⚠️ Não foi possível abrir o navegador automaticamente.")
    print(f"   Abra manualmente: {url}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inicia um servidor local e abre o site no navegador."
    )
    parser.add_argument(
        "--porta",
        "-p",
        type=int,
        default=DEFAULT_PORT,
        help=f"Porta do servidor (padrão: {DEFAULT_PORT}).",
    )
    parser.add_argument(
        "--sem-navegador",
        action="store_true",
        help="Não abrir automaticamente o navegador.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv or sys.argv[1:])
    porta = find_free_port(args.porta)
    if porta != args.porta:
        print(
            f"ℹ️ Porta {args.porta} ocupada. Usando a porta livre mais próxima: {porta}."
        )
    run_server(porta, not args.sem_navegador)


if __name__ == "__main__":
    main()
