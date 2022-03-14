from behave import when, then, given
import time


@when(u'doy click en "Administrar Productos"')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div[2]/header/div[2]/nav/div/ul/li[8]/a').click()
    time.sleep(1)


@when(u'doy click en el boton "Nuevo Producto"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[3]/div/a').click()


@then(u'ingreso el vendedor')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div[3]/div/div/div/form/div[1]/div/div').click()
    context.driver.find_element_by_xpath(
        '/html/body/div[3]/div/div/div/form/div[1]/div/div/ul/li[7]').click()


@then(u'ingreso el nombre "Cinto"')
def step_impl(context):
    context.driver.find_element_by_id('id_nombre').send_keys("Cinto")
    time.sleep(1)


@then(u'el precio "10"')
def step_impl(context):
    context.driver.find_element_by_id('id_precio').send_keys(10)
    time.sleep(1)


@then(u'el stock "50"')
def step_impl(context):
    context.driver.find_element_by_id('id_stock').send_keys(5)
    time.sleep(1)


@then(u'la categoria "Talabarteria"')
def step_impl(context):
    context.driver.find_element_by_id('id_categoria').send_keys("Talabarteria")
    time.sleep(1)


@then(u'una descripcion "Cinto perforado"')
def step_impl(context):
    context.driver.find_element_by_id(
        'id_descripcion').send_keys("Cinto perforado")
    time.sleep(1)


@then(u'presiono el boton de "Agregar"')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '/html/body/div[3]/div/div/div/form/div[8]/button').click()


@then(u'me redirije a la pantalla de lista de articulos')
def step_impl(context):
    pass
