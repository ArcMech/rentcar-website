(function($) {
  "use strict";

  // Mobile dropdown
  $(".has-dropdown>a").on("click", function() {
    $(this)
      .parent()
      .toggleClass("active");
  });

  // Parallax Background
  $.stellar({
    responsive: true
  });
})(jQuery);
