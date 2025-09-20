(function ($) {
  "use strict";

	$(document).on('bumediShopPageInit added_to_cart', function () {
		bumediThemeModule.producthover();
	});

	bumediThemeModule.producthover = function() {
		const container = document.querySelectorAll('.product-thumbnail-gallery');
		if (container !== null) {
			for( var i = 0; i < container.length; i++ ) {
				const self = container[i];
				const selfDuration = Number(self.dataset.duration);
				const selfReset = self.dataset.reset === 'true' ? true : false;
				const selfStyle = self.dataset.style;

				const HoverGallerySlider = new HoverGallery({
				  selector: self,
				  duration: selfDuration,
				  resetHover: selfReset,
				  style: selfStyle
				});
			}
		}
		
	}
	
	$(document).ready(function() {
		bumediThemeModule.producthover();
	});

})(jQuery);
