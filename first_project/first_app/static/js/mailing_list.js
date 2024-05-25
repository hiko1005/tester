import { createApp, ref } from "vue"

class MailingList {
    label;
    contacts;
    is_active = true;
    mailing_services;
    sites;
}

const app = createApp({
    data() {
        return {
            object: ref(new MailingList())
        }
    },
    methods: {
        validate() {
            let result = true
            result = result && this.object.label != null && this.object.label.replaceAll(" ", "").length >= 3;
            result = result && this.object.contacts.length > 0;
            result = result && this.object.mailing_services.length > 0;
            result = result && this.object.sites.length > 0;

            return result
        },
        submitForm() {
            if(!this.validate()) {
                alert('Try again, you wrote something wrong')
            } else {
                fetch(this.$el.parentElement.action, {
                    method: 'POST',
                    body: JSON.stringify(this.object),
                    headers: {
                        "X-CSRFToken": this.$el.parentElement.querySelector('input[name="csrfmiddlewaretoken"]').value
                    }
                }).then(respone => respone.json()).then(data => {
                    location.href = '/app/list/mailing-lists'
                })
            }
        }
    }
})

app.mount("#app")