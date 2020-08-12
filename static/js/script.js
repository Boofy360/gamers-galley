$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $(".dropdown-trigger").dropdown();
    $('.collapsible').collapsible();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 0,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
  });
