#!/usr/bin/env python3
import sys
import textwrap
from collections import namedtuple
import time

import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

import e2e

#Funciones de ayuda
def show(text):
    print(textwrap.dedent(text))

def show_passed():
    print('\033[92m', "    Passed", '\033[0m')

def show_not_passed(e):
    print('\033[91m', "    Not passsed", '\033[0m')
    print(textwrap.indent(str(e), "    "))

# Contexto de las pruebas

Ctx = namedtuple("Ctx", "path process app")

def given_he_lanzado_la_aplicacion(ctx):
    process, app = e2e.run(ctx.path)
    assert app is not None
    return Ctx(path= ctx.path, process= process, app= app)

def then_veo_el_texto_buscar_nombre_vacio(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if
           node.get_role_name() == 'text')
    text = next(gen, None)
    assert text is not None
    assert text.get_name() == "Introducir_nombre"
    return ctx

def then_veo_fecha_inicial_vacia(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if
           node.get_role_name() == 'text' and node.get_name()=='Fecha_inicial')
    text = next(gen, None)
    assert text is not None
    assert text.get_text(0, -1) == ""
    return ctx

def then_veo_fecha_final_vacia(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if
           node.get_role_name() == 'text' and node.get_name()=='Fecha_final')
    text = next(gen, None)
    assert text is not None
    assert text.get_text(0,-1) == ""
    return ctx

def when_selecciono_Luis_Perez(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'text')
    entry = next(gen, None)
    assert entry is not None
    assert entry.get_name() == "Introducir_nombre"
    entry.set_text_contents('Luis Perez')

    return ctx

def when_pulso_boton_buscar_persona(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'push button'
           and node.get_name()=='Boton_buscar_persona')
    button = next(gen, None)
    assert button is not None
    e2e.do_action(button,'click')

    return ctx

def corroborar_datos_Luis_Perez(ctx):
    uuid = "9bea8d38-eb70-4c92-b659-8952e46507d0"
    username = "sadbear831"
    email = "luis.perez@example.com"
    phone = "981-473-053"
    #e2e.dump_tree(ctx.app)
    #Comprobamos ID
    gen0 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
           and node.get_text(0, -1).startswith(uuid))
    tabla = next(gen0, None)
    assert tabla is not None
    #Comprobamos username
    gen1 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
           and node.get_text(0, -1).startswith(username))

    tabla = next(gen1, None)
    assert tabla is not None

    #Comprobamos Name
    gen2 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith("Luis"))

    tabla = next(gen2, None)
    assert tabla is not None

    # Comprobamos Surname
    gen3 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith("Perez"))

    tabla = next(gen3, None)
    assert tabla is not None

    # Comprobamos Email
    gen4 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith(email))

    tabla = next(gen4, None)
    assert tabla is not None

    # Comprobamos Phone
    gen5 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith(phone))

    tabla = next(gen5, None)
    assert tabla is not None

    # Comprobamos isVaccinated
    gen6 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith("True"))

    tabla = next(gen6, None)
    assert tabla is not None

    return ctx

def when_selecciono_Sebastian_Vargas(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'text')
    entry = next(gen, None)
    assert entry is not None
    assert entry.get_name() == "Introducir_nombre"
    entry.set_text_contents('Sebastian Vargas')

    return ctx

def corroborar_datos_Sebastian_Vargas(ctx):
    uuid = "21688b13-499f-42d3-9cb0-254a0bad4251"
    username = "greenleopard140"
    email = "sebastian.vargas@example.com"
    phone = "901-969-603"
    # Comprobamos ID
    gen0 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith(uuid))
    tabla = next(gen0, None)
    assert tabla is not None
    # Comprobamos username
    gen1 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith(username))

    tabla = next(gen1, None)
    assert tabla is not None

    # Comprobamos Name
    gen2 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith("Sebastian"))

    tabla = next(gen2, None)
    assert tabla is not None

    # Comprobamos Surname
    gen3 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith("Vargas"))

    tabla = next(gen3, None)
    assert tabla is not None

    # Comprobamos Email
    gen4 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith(email))

    tabla = next(gen4, None)
    assert tabla is not None

    # Comprobamos Phone
    gen5 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith(phone))

    tabla = next(gen5, None)
    assert tabla is not None

    # Comprobamos isVaccinated
    gen6 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith("True"))

    tabla = next(gen6, None)
    assert tabla is not None

    return ctx

def when_selecciono_fechaInicial_radar(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if
           node.get_role_name() == 'text' and node.get_name() == 'Fecha_inicial')
    entry = next(gen, None)
    assert entry is not None
    assert entry.get_name() == "Fecha_inicial"
    entry.set_text_contents('2021-08-06')

    return ctx

def when_selecciono_fechaFinal_radar(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if
           node.get_role_name() == 'text' and node.get_name() == 'Fecha_final')
    entry = next(gen, None)
    assert entry is not None
    assert entry.get_name() == "Fecha_final"
    entry.set_text_contents('2021-09-10')

    return ctx

def when_pulso_boton_radar(ctx):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'push button'
           and node.get_name() == 'Boton_Alertas_Covid')
    button = next(gen, None)
    assert button is not None
    e2e.do_action(button,'click')

    return ctx

def corroborar_datos_radar(ctx):
    francisca_phone = "989-514-978"
    concepcion_phone ="962-618-846"
    #Francisca
    gen0 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
           and node.get_text(0, -1).startswith("Francisca"))

    tabla = next(gen0, None)
    assert tabla is not None

    gen1 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith(francisca_phone))

    tabla = next(gen1, None)
    assert tabla is not None


    #Como está en la segunda página debemos clickar en el boton para traernos otra página
    gen2 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'push button'
           and node.get_name() == 'Avanzar_alertas_covid')
    boton = next(gen2, None)
    assert boton is not None
    e2e.do_action(boton,'click')

    # Concepcion
    gen3 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith("Concepcion"))
    tabla = next(gen3, None)
    assert tabla is not None

    gen4 = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
            and node.get_text(0, -1).startswith(concepcion_phone))
    tabla = next(gen4, None)

    assert tabla is not None

    return ctx

def step_la_interface_sigue_respondiendo(app: Atspi.Object) -> None:
    # ELiminamos el timeout de arrancar la app
    Atspi.set_timeout(800, -1)
    when_selecciono_Luis_Perez(ctx)
    when_pulso_boton_buscar_persona(ctx)
    corroborar_datos_Luis_Perez(ctx)

if __name__ == '__main__':
    sut_path = sys.argv[1]
    initial_ctx = Ctx(path=sut_path, process=None, app=None)

    show("""
    GIVEN he lanzado la aplicación
    THEN veo el texto "Introduzca un nombre" vacío
    """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = then_veo_el_texto_buscar_nombre_vacio(ctx)
        #e2e.dump_tree(ctx.app)
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)

    show("""
        GIVEN he lanzado la aplicación
        THEN veo las fechas vacías
        """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = then_veo_fecha_inicial_vacia(ctx)
        ctx = then_veo_fecha_final_vacia(ctx)

        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)


    show("""
        GIVEN he lanzado la aplicación
        WHEN introduzco "Luis Perez" y pulso botón de buscar
        THEN compruebo los datos de usuario
        """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_selecciono_Luis_Perez(ctx)
        ctx = when_pulso_boton_buscar_persona(ctx)
        ctx = corroborar_datos_Luis_Perez(ctx)
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)


    show("""
        GIVEN he lanzado la aplicación
        WHEN introduzco "Sebastian Vargas" y pulso botón de buscar
        THEN compruebo los datos de usuario
        """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_selecciono_Sebastian_Vargas(ctx)
        ctx = when_pulso_boton_buscar_persona(ctx)
        ctx = corroborar_datos_Sebastian_Vargas(ctx)
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)
    

    show("""
        GIVEN he lanzado la aplicación
        WHEN busco a Luis Perez e introduzco "2021-08-06" y "2021-09-10"
        y pulso botón de buscar
        THEN compruebo los datos del radar
        """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_selecciono_Luis_Perez(ctx)
        ctx = when_pulso_boton_buscar_persona(ctx)
        ctx = when_selecciono_fechaInicial_radar(ctx)
        ctx = when_selecciono_fechaFinal_radar(ctx)
        ctx = when_pulso_boton_radar(ctx)
        ctx = corroborar_datos_radar(ctx)

        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)

    show("""
        GIVEN he lanzado la aplicación
        WHEN busco a Luis Perez y pulso botón de buscar
        THEN compruebo concurrencia de la app
        """)
    ctx = initial_ctx
    try:
        ctx = given_he_lanzado_la_aplicacion(ctx)
        ctx = step_la_interface_sigue_respondiendo(ctx)
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)


