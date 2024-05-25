import { createApp, ref, watch } from "vue"

class SiteAdd {
    label;
    url = "";
    description;
    expected_responce_code = "";
    expected_responce_code_pattern = "";
    cheking_active = true;
    inversive_condition = true;
    cron_schedule = "* * * * *";
}

const app = createApp({
    data() {
        return {
            object: ref(new SiteAdd())
        }
    },
    methods: {
        validate() {
            let result = true
            result = result && this.object.label != null && this.object.label != ' ' && this.object.label.length > 3
            if (!this.object.url.match(/(?:https?:\/\/)?(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?/)) {
                result = false
            }
            result = result && this.object.description != null && this.object.description.length <= 255 && this.object.description != ' '
            if (!this.object.expected_responce_code.match(/([0-5][0-9][0-9]){1,}/)) {
                result = false
            }
            if (!this.object.cron_schedule.match(/(@(annually|yearly|monthly|weekly|daily|hourly|reboot))|(@every (\d+(ns|us|µs|ms|s|m|h))+)|((((\d+,)+\d+|(\d+(\/|-)\d+)|\d+|\*) ?){5,7})/)) {
                result = false
            }
            result = result && this.object.cron_schedule != null && this.object.cron_schedule != ' ' && this.object.cron_schedule.length >= 9

            return result
        },
        submitForm() {
            if (!this.validate())
                alert('Try again, you wrote something wrong')
            else {
                fetch(this.$el.parentElement.action, {
                    method: "POST",
                    body: JSON.stringify(this.object),
                    headers: {
                        "X-CSRFToken":  this.$el.parentElement.querySelector('input[name="csrfmiddlewaretoken"]').value
                    }
                }).then(respone => respone.json()).then(data => {
                    location.href = '/app/list/sites'
                })
            }
        }
    }
})

app.mount('#app')