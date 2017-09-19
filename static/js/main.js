var app = new Vue({
    el: '#app',
    data: {
        reservations: [],
        show_add_model: false,
        show_next: false
    },
    mounted: function() {
        this.update_reservations()
        if(window.location.hash && window.location.hash.substring(1) == "admin") {
            this.show_next = true;
        }
    },
    methods: {
        update_reservations: function () {
            setTimeout(this.update_reservations, 10000);

            var self=this;
            $.get('/api/reservations').then(function (response) {
                self.reservations = response.reservations;
            });
        },

        add_model: function (form){
            var self=this;
            $.ajax({
                type: 'POST',
                url: '/api/reservations',
                data: JSON.stringify ({name: form.target.name.value}),
                success: function(data) {
                    self.update_reservations();
                    self.show_add_model = false;
                },
                contentType: "application/json",
                dataType: 'json'
            });
        },

        goto_next: function (){
            var self=this;
            $.post('/api/reservations/next').then(function (response) {
                self.reservations = response.reservations;
            });
        }
    }
})
