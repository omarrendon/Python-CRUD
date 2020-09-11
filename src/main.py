import click
from dbConfig import DBConfig

@click.group()
def click_crud():
    pass


@click_crud.command()
@click.option('-nombre_impresora', prompt="Nombre ", type=str, help='Nombre de la impresora')
@click.option('-modelo', prompt="Modelo ", type=str, help='Modelo de la impresora')
@click.option('-marca', prompt="Marca ", type=str, help='Marca de la impresora')
@click.option('-fecha_comprada', prompt="Fecha de compra (DD/MM/YYYY)", type=str, help='Fecha de compra de la impresora')
@click.option('-ultimo_mantenimiento', prompt="Ultimo mantenimiento", type=str, help='Ultimo mantenimineto de la impresora')
@click.option('-ubicacion_fisica', prompt="Ubicación física", type=str, help='Ubicaacion fisica de la impresora')
@click.option('-nombre_responsable', prompt="Nombre del responsable", type=str, help='Nombre del dueño de la impresora')
@click.option('-correo_responsable', prompt="Correo Electronico", type=str, help='Email del dueño de la impresora')
@click.option('-ip', prompt="IP", type=str, help='IP de la impresora')
def crear( nombre_impresora, modelo, marca, fecha_comprada,
                 ultimo_mantenimiento, ubicacion_fisica, nombre_responsable,
                 correo_responsable, ip):
    click.clear()
    ''' Crear una impresora '''  
    impresora = dataBase.create_record(connection, nombre_impresora, modelo, marca,
                               fecha_comprada, ultimo_mantenimiento,
                               ubicacion_fisica, nombre_responsable,
                               correo_responsable, ip)
    if( impresora == 1 ):
        click.echo("\nIMPRESORA CREADA!\n")
        # impresora = dataBase.select_by_name(connection)
        click.echo(impresora)
    else : 
         click.echo(" \nNO SE CREO NADA!\n")
    
    answer_menu()



@click_crud.command()
def listar():
    click.clear()
    ''' Obtener todas las impresoras '''
    impresoras = dataBase.select_records(connection)
    click.echo('\nLISTA DE IMPRESORAS\n')
    click.echo("-"*5)
    click.echo("ID")
    click.echo("-"*5+ "\n")
    
    for impresora in impresoras:
        click.echo(impresora)
    answer_menu()
    


@click_crud.command()
def actualizar():
    ''' Editar información '''
    click.clear()
    click.echo(click.style(("\nID\n"), fg='green'))
    impresora = dataBase.select_records(connection)

    for impresora in impresora:
        click.echo(impresora)
    id_select = click.prompt("\n ID de la impresora a editar", type=str)
    impresora = dataBase.select_by_name(connection, id_select)

    if not impresora:
            click.echo(click.style(("\nNo se encontro la selección"), fg='red') )
    click.clear()
    click.echo(click.style(("\n Presione Enter si no quiere modificar un campo\n"), fg='green')) 
    click.echo(impresora) 

    nombre_impresora= click.prompt('\nNombre a cambiar', default=impresora[1], type=str)
    modelo=click.prompt('Modelo a cambiar',default=impresora[2],type=str)
    marca=click.prompt('Marca a cambiar',default=impresora[3],type=str)
    fecha_comprada=click.prompt('Fecha comprada a cambiar',default=impresora[4],type=str)
    ultimo_mantenimiento=click.prompt('Ultimo mantenimento a cambiar',default=impresora[5],type=str)
    ubicacion_fisica=click.prompt('Ubicación fisica a cambiar',default=impresora[6],type=str)
    nombre_responsable =click.prompt('Nombre del responsable a cambiar',default=impresora[7],type=str)
    correo_responsable =click.prompt('Email a cambiar',default=impresora[8],type=str)
    ip =click.prompt('IP a cambiar',default=impresora[9],type=str)

    impresora = dataBase.update_record(connection, nombre_impresora, modelo, marca,
                      fecha_comprada, ultimo_mantenimiento, ubicacion_fisica,
                      nombre_responsable, correo_responsable, ip, impresora[0],)
    
    click.echo(impresora)
    
    impresora = dataBase.select_by_name(connection, id_select)
    click.echo(impresora)

    answer_menu()




@click_crud.command()
# @click.option('--id', type=str, help='ID unico de la impresora')
def eliminar():
    ''' Elimar una impresora '''
    click.clear()
    click.echo("\nID\n")

    impresoras = dataBase.select_records(connection)
    for impresora in impresoras:
        click.echo(impresora)
    
    id = click.prompt("\nID de la impresora a eliminar", type=int)
    impresoras = dataBase.delete_record(connection, str(id))

    if( impresoras ):
        click.echo("\nFILA:"+" "+str(id)+" "+"ELIMINADA")
    else:
        click.echo("\nFILA NO ENCONTRADA")
    
    answer_menu()




if __name__ == "__main__":
    dataBase = DBConfig()

    connection = dataBase.config_data_base()

    def main_options():
        click.clear()
        print("\nTIENDA DE IMPRESORAS!")
        print("selcecione la opción que deseé ejectuar\n")
        print("OPCIONES"+"\n 1) CREAR REGISTRO DE UNA IMPRESORA"+"\n 2) EDITAR INFO. DE UNA IMPRESORA"+
                "\n 3) MOSTRAR TODAS LAS IMPRESORAS"+"\n 4) ELIMINAR REGISTRO DE UNA IMPRESORA"+"\n 5) SALIR")
        
        opcion = input("\nOPCION : ")

        if(opcion == "1"):
            click_crud( crear() )
        if(opcion == "2"):
            click_crud( actualizar() )
        if(opcion == "3"):
            click_crud( listar() )
        if(opcion == "4"):
            click_crud( eliminar() )
        if( opcion == "5"):
            pass
        else:
            print("OPCIÓN NO VALIDA")

    def answer_menu():
        response = input( "\nVOLVER AL MENU (SI)  SALIR (NO) : ").lower()
        if( response == "si"):
            main_options()
        else:
            if (response == "no"):
                pass
            else:
                print("\nOpnción no valida, intente de nuevo")
                answer_menu()
    main_options()