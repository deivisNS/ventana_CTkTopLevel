def config_alerta(alerta, mensaje):		#recibe 2 parametros  

	top = CTkToplevel(root)
	top.geometry("+310+230")	#posicion donde aparecera en pantalla (+x+y)
	top.overrideredirect(1)		#quitara el marco
	top.attributes("-transparentcolor", "yellow")	#volvera el color amarillo transparente


	marco = CTkFrame(top, fg_color = "black", border_width = 3, corner_radius = 360, 
		border_color = "red", bg_color = "yellow")
	marco.pack()

	
	CTkLabel(marco, text = alerta.upper(), fg_color = "black", text_color = "red",
		justify = "center", font = ("arial black", 20)).grid(row = 0, column = 0, pady = 5, padx = 30)
	CTkLabel(marco, text = mensaje, fg_color = "black", text_color = "white", 
		justify = "left").grid(row = 1, column= 0, pady = 5, padx = 50)


	CTkButton(marco, text = "Cerrar", text_color = "white", border_width = 2, 
		border_color = "white", command = top.destroy).grid(row = 2, column = 0, pady = 10, padx = 30)	


	top.mainloop()
