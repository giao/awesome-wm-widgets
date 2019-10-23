local wibox = require("wibox")
local awful = require("awful")
local naughty = require("naughty")
local watch = require("awful.widget.watch")

local path_to_icons = "/usr/share/icons/Arc/actions/22/"

email_widget = wibox.widget.textbox()
email_widget:set_font('Play 9')

email_icon = wibox.widget.imagebox()
email_icon:set_image(path_to_icons .. "/mail-mark-new.png")

watch(
    --"python /home/giao/.config/awesome/awesome-wm-widgets/email-widget/count_unread_emails_xdays.py", 20,
    "python /home/giao/.config/awesome/awesome-wm-widgets/email-widget/count_unread_emails.py", 300,
    function(widget, stdout, stderr, exitreason, exitcode)
        local unread_emails_num = tonumber(stdout) or -1
        if (unread_emails_num > 0) then
        	--email_icon:set_image(path_to_icons .. "/mail-mark-unread.png")
        	email_icon:set_image(path_to_icons .. "star.png")
	        email_widget:set_text(stdout)
        elseif (unread_emails_num == 0) then
        	email_icon:set_image(path_to_icons .. "/mail-message-new.png")
        	--email_icon:set_image(path_to_icons .. "exit.png")
   	      email_widget:set_text("")
        else
        	email_icon:set_image(path_to_icons .. "exit.png")
   	      email_widget:set_text("cant access mail server ?")
        end	
    end
)


function show_emails()
    awful.spawn.easy_async([[bash -c 'python /home/giao/.config/awesome/awesome-wm-widgets/email-widget/read_unread_emails_xdays.py']],
        function(stdout, stderr, reason, exit_code)   
            naughty.notify{
                text = stdout,
                title = "Unread Emails",
                timeout = 5, hover_timeout = 0.5,
                width = 400,
            }
        end
    )
end

email_icon:connect_signal("mouse::enter", function() show_emails() end)
