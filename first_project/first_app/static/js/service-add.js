import {createApp, ref, watch} from "vue"

class Service {
    label;
    type;
    token;
    message_pattern;
    is_active;
    login;
    password;
    headers;
    api_url;
    request_type;
    body_pattern;
}

const app = createApp({
    data() {
        return {
            object: ref(new Service()),
            contacts: ref([])    
        }
    },
    methods: {
        validate() {
            let result = true
            result = result && this.object.label!=null && this.object.label!=' ' && this.object.label.length>=3
            if(this.object.type.value == "Telegram" && this.object.token)
            result = result && this.object.token!=' '
            if(this.object.type.value == "Telegram" || this.object.type.value == "e-mail")
            result = result && this.object.message_pat!=null && this.object.message_pat.length <= 255
            if(this.object.type.value == "e-mail" || this.object.type.value == "custom" && this.object.login && this.object.password) {
                result = result && this.object.login!=' ' && this.object.login.length >= 3
                result = result && this.object.password!=' ' && this.object.password.length >= 6
            }
            if(this.object.type.value == "custom" && this.object.headers) {
                result = result && this.object.headers!=' ' && this.object.headers.length <= 255
                if(this.object.api_url.match(/(?:https?:\/\/)?(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?/))
                result = result
            }
            if(this.object.type.value == "custom" && this.object.request_type.value == "POST" && this.object.body_pat)
            result = result && this.object.body_pat!=' ' && this.object.body_pat.length <= 255

            if(this.object.type.value == "Telegram") {
                let pattern = /[0-9]{6}:[a-zA-Z0-9]{3}-[a-zA-Z0-9]{12}-[a-zA-Z0-9]{17}/;
                result = result && pattern.test(this.object.token)
            }
            return result
        },
        submitForm() {

            if(!this.validate()) {
                alert('Try again, you wrote something wrong')
            } else {
                fetch(this.$el.parentElement.action, {
                    method: isEditMode() ? 'PUT':'POST',
                    body: JSON.stringify(this.normalize(this.object)),
                    headers: {
                        "X-CSRFToken": this.$el.parentElement.querySelector('input[name="csrfmiddlewaretoken"]').value
                    }
                }).then(
                    respone => respone.json()
                    
                    )
                    //.then(respone => respone.json())
                    .then(data => {
                        location.href = '/app/list/services'
                    })
            } 
        },
        fetch_contacts() {
            return [
                {label: 'contact1', id: 1},
                {label: 'contact2', id: 2},
                {label: 'contact3', id: 3}
            ];
        },
        normalize(obj) {
            if(obj.type != "Telegram")
                return obj
            if(this.object.type == "Telegram") {
                let n_obj = this.object
                n_obj.type == "custom"
                n_obj.api_url = `https://api.telegram.org/bot{token}/sendMessage`
                n_obj.request_type = "POST"
                n_obj.body_pattern = "{\"chat_id\": \"{contact.contact_string}\", \"text\": \"{message}\"}"
                return n_obj
            }
        }
    },
    mounted() {
        if(isEditMode()) {
            fetch("/app/services?id=" + document.querySelector("input[name = 'id']").value).then(responce => responce.json()).then(data => this.object = data)
        }
    }
})

app.mount("#app")