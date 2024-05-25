import {createApp, ref, watch} from "vue"

class ContactAdd {
    label = "";
    contact_string = "";
    is_active = true;
}

const app = createApp({
    data() {
        return {
            object: ref(new ContactAdd())
        }
    },
    methods: {
        validate() {
            let result = true
            result = result && this.object.label!=null && this.object.label.trim().length!=0 && 3 <= this.object.label.length && this.object.label.length <= 255
            result = result && this.object.contact_string!=null && this.object.contact_string!=' ' && this.object.contact_string.length <= 255

            return result
        },
        submitForm() {
            if(!this.validate())
            alert('Try again, you`re wrote something wrong')
            else {
                fetch(this.$el.parentElement.action, {
                    method: "POST",
                    body: JSON.stringify(this.object),
                    headers: {
                        "X-CSRFToken": this.$el.parentElement.querySelector('input[name="csrfmiddlewaretoken"]').value,
                    }
                }).then(respone => respone.json()).then(data => {
                    location.href = '/app/list/contacts'
                })
            }
            }
        }
    })

app.mount("#app")