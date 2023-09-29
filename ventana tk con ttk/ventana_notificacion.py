
def ventana_alerta_tk(alerta, mensaje):
		
	top_alerta = Toplevel()
	top_alerta.overrideredirect(1)
	top_alerta.geometry(f"+400+250")


	marco = Frame(top_alerta, bd = 4, relief = "solid", bg = "white", pady = 10, padx = 10)
	marco.pack()


	Label(marco, text = alerta.upper(), bg = "white", fg = "red", font = ("arial black", 18)).pack(side = TOP)


	if mensaje != "":
		Label(marco, text = mensaje, bg = "white", fg = "black", font = ("verdana", 10)).pack(padx = 50)


	ttk.Button(marco, text = "Cerrar", style = "config.TButton", takefocus = False, 
		command = top_alerta.destroy).pack(side = BOTTOM)
	
