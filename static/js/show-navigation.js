AFRAME.registerComponent('show-navigation', {

    schema :{

        target: { type: "selector"},
        hide: { type: "selector"},
        name: { type: "string"}
    },

    init: function() {

        var data = this.data;
        var el = this.el;

      el.addEventListener("click", function () {


           var target = data.target;

           var hideTarget = document.querySelectorAll(".sub-control");

           console.log(hideTarget);

            if (hideTarget) {

                    hideTarget.forEach( function(v, i) {

                        v.setAttribute("visible", "false");

                    })

            }

            if (target) {
                target.setAttribute("visible", "true");
            }


    });

    }

})
