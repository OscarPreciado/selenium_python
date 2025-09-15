from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = 'https://nuxqa5.avtest.ink/es/'

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get(URL)
# btn_aliados = driver.find_element(By.ID, 'nonAvFly')
# btn_aliados.click()

# time.sleep(2)


# BUSQUEDA EN LA HOME

select_origin = driver.find_element(By.ID, 'originStationSelected')
print(select_origin.text)

time.sleep(1)

#btn_cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
#btn_cookies.click()

#time.sleep(2)

field_destination = driver.find_element(By.ID,"arrivalStationInputId").click()
time.sleep(1)

select_destination_xpath = '//*[@id="arrivalStationsListId"]/li[8]/button'
select_destination = driver.find_element(By.XPATH, select_destination_xpath).click()
time.sleep(1)

# # DESPLEGAR SELECTOR PASAJEROS

field_passengers_xpath = '//*[@id="searchContentId_RT"]/div[3]/pax-control-custom/div/div/div[2]/div/button'
field_passengers = driver.find_element(By.XPATH, field_passengers_xpath).click()

time.sleep(1)

# # Selector de pasajeros (soon)

#adt_button_xpath = '//*[@id="paxControlSearchId"]/div/div[2]/div[1]/ul/li[1]/div[2]/ibe-minus-plus/div/button[2]'
#adt_button = driver.find_element(By.XPATH, adt_button_xpath)
#adt_button.click()
#time.sleep(2)
#adt_button.click()

search_button = driver.find_element(By.ID, 'searchButton').click()
time.sleep(12)

# SELECT FLIGHT

# Boton de filtro mejor precio
better_price_xpath = '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[1]/journey-filter-control-custom/div/ul/li/div'
better_price = driver.find_element(By.XPATH, better_price_xpath).click()

time.sleep(2)

# Seleccionar journey ida

departure_flight_xpath = '/html/body/div[1]/main/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[2]/div[1]/journey-control-custom/div/div/div[1]/div[2]/button'
departure_flight = driver.find_element(By.XPATH, departure_flight_xpath).click()

time.sleep(3)

# Seleccionar tarifa ida

fare_selection_xpath = '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[2]/div/journey-control-custom/div/div/div[2]/div/div/div/div[1]'
fare_selection = driver.find_element(By.XPATH, fare_selection_xpath).click()
time.sleep(15)

#Seleccionar journey vuelta

arrival_flight_xpath = '/html/body/div[1]/main/div/div[2]/div/div/journey-availability-select-container/div[2]/price-journey-select-custom/div[2]/div[2]/div[1]/journey-control-custom/div/div/div[1]/div[2]/button'
arrival_flight = driver.find_element(By.XPATH, arrival_flight_xpath).click()

time.sleep(2)

#Seleccionar tarifa vuelta

fare_selection_xpath = '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[2]/div/journey-control-custom/div/div/div[2]/div/div/div/div[2]'
fare_selection = driver.find_element(By.XPATH, fare_selection_xpath).click()
time.sleep(5)

# Btn confirmar tarifa (Solo prod)

#fare_continue_xpath = '//*[@id="FB310"]/div[3]/div[1]'
#fare_continue = driver.find_element(By.XPATH, fare_continue_xpath)
#fare_continue.click()
#time.sleep(5)

# BTN CONTINUAR A PASSENGERS

selected_flights_xpath = '//*[@id="maincontent"]/div/div[2]/div/div/button-container/div/div/button'
selected_flights = driver.find_element(By.XPATH, selected_flights_xpath).click()
time.sleep(5)

# LLENAR DATOS DE PASAJERO


#Genero
passenger_gender_xpath = '//*[@id="maincontent"]/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div/personal-data-form-custom/div/form/div/div[1]/div/div[1]/ibe-select-custom/div/div[2]'
passenger_gender = driver.find_element(By.XPATH, passenger_gender_xpath).click()

time.sleep(1)

passenger_gender_selected_xpath = '//*[@id="maincontent"]/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div/personal-data-form-custom/div/form/div/div[1]/div/div[1]/ibe-select-custom/div/div[2]/ul/li[2]/button'
passenger_gender_selected = driver.find_element(By.XPATH, passenger_gender_selected_xpath).click()

time.sleep(1)

#Nombre
passenger_name_xpath = '//*[@id="maincontent"]/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div/personal-data-form-custom/div/form/div/div[1]/div/div[2]/ibe-input/div/div/input'
passenger_name = driver.find_element(By.XPATH, passenger_name_xpath).send_keys("Prueba Newshore")

time.sleep(1)

#Apellido
passenger_lastname_xpath = '//*[@id="maincontent"]/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div/personal-data-form-custom/div/form/div/div[2]/ibe-input/div/div/input'
passenger_lastname = driver.find_element(By.XPATH, passenger_lastname_xpath).send_keys("digital")

#Fecha de nacimiento
birth_day_xpath = '/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[1]/ibe-select-custom/div/div[2]/button'
birth_day = driver.find_element(By.XPATH, birth_day_xpath).click()

birth_day_selected_xpath = '/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[1]/ibe-select-custom/div/div[2]/ul/li[21]/button'
birth_day_selected = driver.find_element(By.XPATH, birth_day_selected_xpath).click()

time.sleep(1)

birth_month_xpath = '/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[2]/ibe-select-custom/div/div[2]/button'
birth_month = driver.find_element(By.XPATH, birth_month_xpath).click()

birth_month_selected_xpath = '/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[2]/ibe-select-custom/div/div[2]/ul/li[6]/button'
birth_month_selected = driver.find_element(By.XPATH, birth_month_selected_xpath).click()

time.sleep(1)

birth_year_xpath = '/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[3]/ibe-select-custom/div/div[2]/button'
birth_year = driver.find_element(By.XPATH, birth_year_xpath).click()

birth_year_selected_xpath = '/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[3]/ibe-select-custom/div/div[2]/ul/li[17]/button'
birth_year_selected = driver.find_element(By.XPATH, birth_year_selected_xpath).click()

time.sleep(1)

#nacionalidad
passenger_country_xpath = '/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[4]/ibe-select-custom/div/div[2]/button'
passenger_country = driver.find_element(By.XPATH, passenger_country_xpath).click()

time.sleep(3)

passenger_country_selected_xpath = '/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[4]/ibe-select-custom/div/div[2]/ul/li[1]'
passenger_country_selected = driver.find_element(By.XPATH, passenger_country_selected_xpath).click()

time.sleep(2)

# TITULAR DE LA RESERVA

prefix_selector = driver.find_element(By.ID, 'phone_prefixPhoneId').click()

time.sleep(1)

prefix_selected = driver.find_element(By.ID, 'phone_prefixPhoneId-0').click()

time.sleep(1)

titular_phone = driver.find_element(By.ID, 'phone_phoneNumberId').send_keys("1234567890")

time.sleep(1)

titular_email = driver.find_element(By.ID, 'email').send_keys("accept@accept.com")

time.sleep(1)

titular_email = driver.find_element(By.ID, 'confirmEmail').send_keys("accept@accept.com")
time.sleep(1)

#Btn checkbox solo prod
#privacy_checkbox = driver.find_element(By.ID, 'acceptNewCheckbox')
#privacy_checkbox.click()

#time.sleep(1)

btn_continuePassengers_xpath = '//*[@id="maincontent"]/div/div[3]/div/div/button-container/div/div/button'
btn_continuePassengers = driver.find_element(By.XPATH, btn_continuePassengers_xpath).click()

time.sleep(25)

# SERVICES (travel assistance)

travel_assistance_xpath = '//*[@id="maincontent"]/div/div[5]/div/div/service-card-container/div/div[4]/card-component/div'
travel_assistance = driver.find_element(By.XPATH, travel_assistance_xpath).click()

travel_assistance_selected_xpath = '/html/body/ngb-modal-window/div/div/div/div/div[2]/ns-service-selector-custom/div/div[2]/div/div[2]/ns-service-details-custom/div/div/div/div/div/div/div/div/div/service-item-custom/div/div/div[6]/div/div/label'
travel_assistance_selected = driver.find_element(By.XPATH, travel_assistance_selected_xpath).click()
time.sleep(2)

assistance_checkbox = driver.find_element(By.ID, 'termsconditions').click()
time.sleep(2)

btn_confirm_assistance_xpath = '/html/body/ngb-modal-window/div/div/div/div/div[2]/ns-service-selector-custom/div/div[3]/amount-summary-button/div/div/div[2]/ds-button[2]/button'
btn_confirm_assistance = driver.find_element(By.XPATH, btn_confirm_assistance_xpath).click()
time.sleep(10)

#continuar a seatmap

btn_continueServices_xpath = '//*[@id="maincontent"]/div/div[6]/div/div/button-container/div/div/button'
btn_continueServices = driver.find_element(By.XPATH, btn_continueServices_xpath).click()

time.sleep(15)

# SEATMAP

#seleccionar asiento premium
seat_premium = driver.find_element(By.ID, '1A_PREMIUM').click()
time.sleep(7)

#continuar a pagos

btn_continueSeatmap_xpath = '//*[@id="maincontent"]/div/div[4]/div/div/amount-summary-button-container/amount-summary-button/div/div/div[2]/ds-button[2]'
btn_continueSeatmap = driver.find_element(By.XPATH, btn_continueSeatmap_xpath).click()

time.sleep(6)
btn_cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
time.sleep(6)

# PAYMENT

## Ingresa a iframe de pci
iframe_pagos = driver.find_element(By.CLASS_NAME, 'payment-forms-layout_iframe')
driver.switch_to.frame(iframe_pagos)
time.sleep(2)
# Nombre tarjeta

card_name = driver.find_element(By.ID, 'Holder')
card_name.send_keys("ns test")
time.sleep(2)

#Numero tarjeta
card_data = driver.find_element(By.ID, 'Data')
card_data.send_keys("4444333322221111")
time.sleep(1)

#Expiration data
card_expiration = driver.find_element(By.ID, 'expirationMonth_ExpirationDate').click()

time.sleep(1)

card_expiration_selected = driver.find_element(By.ID, 'expirationMonth_ExpirationDate-12').click()

time.sleep(1)

card_year_expiration = driver.find_element(By.ID, 'expirationYear_ExpirationDate').click()

time.sleep(1)

card_year_expiration_selected = driver.find_element(By.ID, 'expirationYear_ExpirationDate-25').click()

time.sleep(1)

card_cvv = driver.find_element(By.ID, 'Cvv').send_keys("123")

driver.switch_to.default_content()

time.sleep(5)

#email
payment_email = driver.find_element(By.ID, 'email').send_keys("accept@accept.com")

time.sleep(1)

#Address

payment_address = driver.find_element(By.ID, 'address').send_keys("address")

time.sleep(1)

#City

payment_city = driver.find_element(By.ID, 'city').send_keys("city")

time.sleep(1)

#Country

billing_country = driver.find_element(By.ID, 'country').click()

time.sleep(1)

billing_selected_country = driver.find_element(By.ID, 'country-42').click()

#time.sleep(1)

#State (solo prod)

#billing_state = driver.find_element(By.ID, 'state')
#billing_state.click()

#time.sleep(1)

#billing_selected_state = driver.find_element(By.ID, 'state-5')
#billing_selected_state.click()

#time.sleep(1)

#Zipcode (solo prod)

#payment_zipcode = driver.find_element(By.ID, 'code')
#payment_zipcode.click()
#payment_zipcode.send_keys("12345")

time.sleep(1)

#Checkbox

payment_tyc_checkbox = driver.find_element(By.ID, 'terms').click()

time.sleep(3)

# Btn pay

btn_pay_xpath = '/html/body/dcx-content-body/div/div/div[3]/div/div[1]/div/div[2]/dcx-component/div/div[2]/div/action-button/ds-button/button'
btn_pay = driver.find_element(By.XPATH, btn_pay_xpath).click()

time.sleep(60)
