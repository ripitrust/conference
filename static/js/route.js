AFRAME.registerComponent('route', {


    schema: {

        location: {type: "string"},
        index: {type: "boolean"}

    },


    init: function() {


        var data = this.data;
        var el = this.el;

        var location = data.location;

        var routes = window.routes || {};

        routes[location] = this.el;

        window.routes = routes;


        window.onpopstate = function(e) {


            var routes = window.routes;

            console.log(e.state);




        } ;




    },



});