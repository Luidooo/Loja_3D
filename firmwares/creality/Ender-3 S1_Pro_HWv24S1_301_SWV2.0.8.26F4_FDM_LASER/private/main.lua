local powerOn = 1
function main(screen)
    
    if powerOn == 1
    then
        powerOn = 0
        set_auto_notify(1);
        set_uint16(0x110e,0000)
    end
end