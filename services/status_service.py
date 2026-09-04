def gerar_status(links):
    pastas_faltantes = []
    
    for pasta, link in links.items():
        if not link:
            pastas_faltantes.append(pasta)
            
    if pastas_faltantes:
        return f"Faltando links para as pastas: {', '.join(pastas_faltantes)}"
    
    return "OK"