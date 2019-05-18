''''
agenda_pacientes = []
agenda1 = [('Juan', 'Mora', 100103111, 'Heredia', 81118811, ('Cancer', 'Gripe'), ('mediacament_uno'), ('medicamento_dos')),
('Ana', 'Jimenez', 32415116, 'San jose', 46261266, 'consulta',('Sarampeon'), ('medicamento_tres')),
('Sofia', 'Alfaro', 32415116, 'Alajuela', 51161161, 'consulta', ('tumores','Gripe'), ('medicamento_dos')),
('Carlos', 'Sanchez', 33411151, 'Cartago', 41655161, 'dolor',('Sarampeon', 'Diabetes', 'Gripe'), ('medicamento_cinco'))]

print(agenda_pacientes.extend(agenda1))

print('En total llegaron', len(agenda_pacientes), 'pacientes')

print(agenda1.update('sofia', 'alfaro', 135654899, 'Heredia', 897646, ('Migraña'), ('Medicamento uno')))
'''
pass

agenda = {{'nombre': 'Juan Mora','Ana Jimenez', 'Sofis Alfaro', 'Carlos Sanchez'},
{'Identificacion': '1216464', '654684984', '5165484', '165494'},
{'Direccion': 'Heredia', 'San Jose', 'Alajuela', 'Perez Zeledon'},
{'telefono': '215466', '5644698', '545465', '4987984'},
{'enfermedades' : ('cancer,', 'Gripe'), ('Sarampeon'), ('Diabetes', 'Gripe'), ('Migrañas')},
{'Medicamentos': ('uno','tres'), ('dos','tres','cinco',), ('cinco'),('uno', 'dos')}}

pass

