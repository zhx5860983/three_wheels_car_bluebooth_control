def on_mes_dpad_controller_id_button_4_down():
    global velo_multiplier_r, full_speed, velo_multiplier_l
    if straight_pressed:
        velo_multiplier_r = 0.3
    else:
        full_speed = speed_limit
        velo_multiplier_r = -0.4
        velo_multiplier_l = 0.4
    set_target_velo()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_4_DOWN,
    on_mes_dpad_controller_id_button_4_down)

def on_mes_dpad_controller_id_button_4_up():
    global full_speed, velo_multiplier_l, velo_multiplier_r
    if not (straight_pressed):
        full_speed = 0
    velo_multiplier_l = 1
    velo_multiplier_r = 1
    set_target_velo()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_4_UP,
    on_mes_dpad_controller_id_button_4_up)

def on_mes_dpad_controller_id_button_3_up():
    global full_speed, velo_multiplier_l, velo_multiplier_r
    if not (straight_pressed):
        full_speed = 0
    velo_multiplier_l = 1
    velo_multiplier_r = 1
    set_target_velo()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_3_UP,
    on_mes_dpad_controller_id_button_3_up)

def on_button_pressed_a():
    global start
    start = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def set_target_velo():
    global velo_l_target, velo_r_target
    velo_l_target = full_speed * velo_multiplier_l
    velo_r_target = full_speed * velo_multiplier_r

def on_mes_dpad_controller_id_button_a_down():
    wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 80)
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_A_DOWN,
    on_mes_dpad_controller_id_button_a_down)

def on_mes_dpad_controller_id_button_1_up():
    global straight_pressed, full_speed
    straight_pressed = 0
    full_speed = 0
    set_target_velo()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_1_UP,
    on_mes_dpad_controller_id_button_1_up)

def on_mes_dpad_controller_id_button_3_down():
    global velo_multiplier_l, full_speed, velo_multiplier_r
    if straight_pressed:
        velo_multiplier_l = 0.3
    else:
        full_speed = speed_limit
        velo_multiplier_l = -0.4
        velo_multiplier_r = 0.4
    set_target_velo()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_3_DOWN,
    on_mes_dpad_controller_id_button_3_down)

def on_button_pressed_ab():
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global start, velo_l, velo_r, velo_multiplier_l, velo_multiplier_r
    start = 0
    velo_l = 0
    velo_r = 0
    velo_multiplier_l = 1
    velo_multiplier_r = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_mes_dpad_controller_id_button_2_up():
    global straight_pressed, full_speed
    straight_pressed = 0
    full_speed = 0
    set_target_velo()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_2_UP,
    on_mes_dpad_controller_id_button_2_up)

def on_mes_dpad_controller_id_button_2_down():
    global straight_pressed, full_speed
    straight_pressed = 1
    full_speed = 0 - speed_limit
    set_target_velo()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_2_DOWN,
    on_mes_dpad_controller_id_button_2_down)

def on_mes_dpad_controller_id_button_a_up():
    wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 140)
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_A_UP,
    on_mes_dpad_controller_id_button_a_up)

def on_mes_dpad_controller_id_button_1_down():
    global straight_pressed, full_speed
    straight_pressed = 1
    full_speed = speed_limit
    set_target_velo()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_1_DOWN,
    on_mes_dpad_controller_id_button_1_down)

time_last = 0
dt = 0
time_current = 0
velo_r = 0
velo_l = 0
velo_r_target = 0
velo_l_target = 0
start = 0
velo_multiplier_l = 0
full_speed = 0
velo_multiplier_r = 0
straight_pressed = 0
speed_limit = 0
speed_limit = 100
acceleration_time = 1000.0
inv_acceleration_time = 1.0 / acceleration_time
bluetooth.start_button_service()
bluetooth.start_led_service()

def on_forever():
    global time_current, dt, time_last, velo_l, velo_r
    if start:
        time_current = input.running_time()
        dt = 1000
        time_last = time_current
        velo_l = velo_l + inv_acceleration_time * (velo_l_target - velo_l) * dt
        velo_r = velo_r + inv_acceleration_time * (velo_r_target - velo_r) * dt
        wuKong.set_all_motor(velo_l, velo_r)
    else:
        basic.clear_screen()
basic.forever(on_forever)
