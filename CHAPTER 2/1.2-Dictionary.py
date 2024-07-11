    #criando um dicionario de variaveis 
    
bin_colors = {
    "manual_colo": "Yellow",
    "approved_color": "Green",
    "refused_color": "Red"
}

print(bin_colors)
print(bin_colors.get('approved_color'))
print(bin_colors['approved_color'])
bin_colors['approved_color'] = "Purple" #trocando o valor da variavel
print(bin_colors)


