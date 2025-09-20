(function ($) {
  "use strict";

	$(document).on('bumediShopPageInit added_to_cart', function () {
		bumediThemeModule.filterproducts();
	});

	bumediThemeModule.filterproducts = function() {
	    $(function() {
			$(".filter-wide-button .dropdown-toggle").on("click", function() { 
			$(".filter-wide-button .dropdown-menu").toggleClass('open'); });
		});
	}
	
	$(document).ready(function() {
		bumediThemeModule.filterproducts();
	});

}(jQuery));