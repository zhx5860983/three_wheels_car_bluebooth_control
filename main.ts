control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_4_DOWN, function () {
    if (straight_pressed) {
        velo_multiplier_r = 0.2
    } else {
        full_speed = speed_limit
        velo_multiplier_r = -0.3
        velo_multiplier_l = 0.3
    }
    set_target_velo()
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_4_UP, function () {
    if (!(straight_pressed)) {
        full_speed = 0
    }
    velo_multiplier_l = 1
    velo_multiplier_r = 1
    set_target_velo()
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_3_UP, function () {
    if (!(straight_pressed)) {
        full_speed = 0
    }
    velo_multiplier_l = 1
    velo_multiplier_r = 1
    set_target_velo()
})
input.onButtonPressed(Button.A, function () {
    start = 1
})
function set_target_velo () {
    velo_l_target = full_speed * velo_multiplier_l
    velo_r_target = full_speed * velo_multiplier_r
}
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_A_DOWN, function () {
    wuKong.setServoAngle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 80)
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_1_UP, function () {
    straight_pressed = 0
    full_speed = 0
    set_target_velo()
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_3_DOWN, function () {
    if (straight_pressed) {
        velo_multiplier_l = 0.2
    } else {
        full_speed = speed_limit
        velo_multiplier_l = -0.3
        velo_multiplier_r = 0.3
    }
    set_target_velo()
})
input.onButtonPressed(Button.AB, function () {
    control.reset()
})
input.onButtonPressed(Button.B, function () {
    start = 0
    velo_l = 0
    velo_r = 0
    velo_multiplier_l = 1
    velo_multiplier_r = 0
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_2_UP, function () {
    straight_pressed = 0
    full_speed = 0
    set_target_velo()
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_2_DOWN, function () {
    straight_pressed = 1
    full_speed = 0 - speed_limit
    set_target_velo()
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_A_UP, function () {
    wuKong.setServoAngle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 200)
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_1_DOWN, function () {
    straight_pressed = 1
    full_speed = speed_limit
    set_target_velo()
})
let dt = 0
let time_current = 0
let time_last = 0
let velo_r = 0
let velo_l = 0
let velo_r_target = 0
let velo_l_target = 0
let start = 0
let full_speed = 0
let straight_pressed = 0
let velo_multiplier_r = 0
let velo_multiplier_l = 0
let speed_limit = 0
speed_limit = 100
let acceleration_time = 50
let inv_acceleration_time = 1 / acceleration_time
velo_multiplier_l = 1
velo_multiplier_r = 1
bluetooth.startButtonService()
bluetooth.startLEDService()
basic.forever(function () {
    if (start) {
        if (time_last == 0) {
            time_current = input.runningTime()
        }
        time_current = input.runningTime()
        dt = time_current - time_last
        time_last = time_current
        velo_l = velo_l + inv_acceleration_time * (velo_l_target - velo_l) * dt
        velo_r = velo_r + inv_acceleration_time * (velo_r_target - velo_r) * dt
        wuKong.setAllMotor(velo_r, velo_l)
    } else {
        basic.clearScreen()
    }
})
