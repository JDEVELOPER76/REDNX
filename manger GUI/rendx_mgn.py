import threading
import tkinter as tk
from tkinter import ttk, messagebox

import uvicorn

from obip import obtener_ip
from server import app


class ServerGUI:
	def __init__(self, root: tk.Tk) -> None:
		self.root = root
		self.root.title("RENDX Server GUI")
		self.root.geometry("420x220")
		self.root.resizable(False, False)

		self.server: uvicorn.Server | None = None
		self.server_thread: threading.Thread | None = None
		self.is_running = False

		self._build_ui()

	def _build_ui(self) -> None:
		main = ttk.Frame(self.root, padding=16)
		main.pack(fill=tk.BOTH, expand=True)

		title = ttk.Label(main, text="Control del servidor", font=("Segoe UI", 14, "bold"))
		title.pack(anchor=tk.W)

		self.status_var = tk.StringVar(value="Estado: detenido")
		status = ttk.Label(main, textvariable=self.status_var)
		status.pack(anchor=tk.W, pady=(8, 12))

		btns = ttk.Frame(main)
		btns.pack(fill=tk.X)

		self.btn_local = ttk.Button(btns, text="Iniciar Local", command=self.start_local)
		self.btn_local.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 6))

		self.btn_lan = ttk.Button(btns, text="Iniciar LAN", command=self.start_lan)
		self.btn_lan.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(6, 0))

		self.btn_stop = ttk.Button(main, text="Detener", command=self.stop_server, state=tk.DISABLED)
		self.btn_stop.pack(fill=tk.X, pady=(12, 0))

		info = ttk.Label(
			main,
			text="Puertos: 8000\nLocal: http://127.0.0.1:8000",
			foreground="#555",
		)
		info.pack(anchor=tk.W, pady=(12, 0))

	def _start_server_thread(self, host: str) -> None:
		if self.is_running:
			messagebox.showinfo("Servidor", "El servidor ya está en ejecución.")
			return

		config = uvicorn.Config(app, host=host, port=8000, log_level="info")
		self.server = uvicorn.Server(config)

		self.server_thread = threading.Thread(target=self._run_server, daemon=True)
		self.server_thread.start()

		self.is_running = True
		self.btn_local.configure(state=tk.DISABLED)
		self.btn_lan.configure(state=tk.DISABLED)
		self.btn_stop.configure(state=tk.NORMAL)

	def _run_server(self) -> None:
		if self.server:
			self.server.run()

	def start_local(self) -> None:
		self.status_var.set("Estado: iniciando (local)")
		self._start_server_thread("127.0.0.1")
		self.status_var.set("Estado: en ejecución (local)")

	def start_lan(self) -> None:
		ip = obtener_ip()
		self.status_var.set(f"Estado: iniciando (LAN {ip})")
		self._start_server_thread("0.0.0.0")
		self.status_var.set(f"Estado: en ejecución (LAN {ip})")

	def stop_server(self) -> None:
		if not self.is_running or not self.server:
			return

		self.status_var.set("Estado: deteniendo...")
		self.server.should_exit = True

		self.is_running = False
		self.btn_local.configure(state=tk.NORMAL)
		self.btn_lan.configure(state=tk.NORMAL)
		self.btn_stop.configure(state=tk.DISABLED)
		self.status_var.set("Estado: detenido")


def main() -> None:
	root = tk.Tk()
	ServerGUI(root)
	root.mainloop()


if __name__ == "__main__":
	main()




