/* KLB Addons for Elementor v1.0 */

jQuery.noConflict();
!(function ($) {
	"use strict";

	
	/* CAROUSEL*/
	function klb_carousel($scope, $) {
		const container = document.querySelectorAll('.site-slider');
		if (container !== null) {
			container.forEach((slider) => {
			  let slider_items = Number(slider.dataset.items);
			  let slider_items_xxl = Number(slider.dataset.xxl);
			  let slider_items_xl = Number(slider.dataset.xl);
			  let slider_items_lg = Number(slider.dataset.lg);
			  let slider_items_md = Number(slider.dataset.md);
			  let slider_items_sm = Number(slider.dataset.sm);
			  let slider_items_xs = Number(slider.dataset.xs);
			  let slider_items_to = Number(slider.dataset.itemsscroll) ? Number(slider.dataset.itemsscroll) : 1;
			  let slider_speed = Number(slider.dataset.speed);

			  let slider_arrows = slider.dataset.arrows === 'true' ? true : false;
			  let slider_arrows_xxl = slider.dataset.arrowsXxl === 'true' ? true : false;
			  let slider_arrows_xl = slider.dataset.arrowsXl === 'true' ? true : false;
			  let slider_arrows_lg = slider.dataset.arrowsLg === 'true' ? true : false;
			  let slider_arrows_md = slider.dataset.arrowsMd === 'true' ? true : false;
			  let slider_arrows_sm = slider.dataset.arrowsSm === 'true' ? true : false;
			  let slider_arrows_xs = slider.dataset.arrowsXs === 'true' ? true : false;

			  let slider_dots = slider.dataset.dots === 'true' ? true : false;
			  let slider_dots_xxl = slider.dataset.dotsXxl === 'true' ? true : false;
			  let slider_dots_xl = slider.dataset.dotsXl === 'true' ? true : false;
			  let slider_dots_lg = slider.dataset.dotsLg === 'true' ? true : false;
			  let slider_dots_md = slider.dataset.dotsMd === 'true' ? true : false;
			  let slider_dots_sm = slider.dataset.dotsSm === 'true' ? true : false;
			  let slider_dots_xs = slider.dataset.dotsXs === 'true' ? true : false;
			  
			  let slider_autoplay = slider.dataset.autoplay === 'true' ? true : false;
			  let slider_auto_speed = Number(slider.dataset.autospeed);

			  let slider_fade = slider.dataset.fade === 'true' ? true : false;

			  let slider_as_nav_for = slider.dataset.assfornav;
			  let slider_focus_on_select = slider.dataset.focusonselect === 'true' ? true : false;
			  let slider_vertical = slider.dataset.vertical === 'true' ? true : false;

			  let args = {
				slidesToShow: slider_items,
				slidesToScroll: slider_items_to,
				speed: slider_speed,
				arrows: slider_arrows,
				dots: slider_dots,
				autoplay: slider_autoplay,
				autoplaySpeed: slider_auto_speed,
				asNavFor: slider_as_nav_for,
				focusOnSelect: slider_focus_on_select,
				vertical: slider_vertical,
				fade: slider_fade,
				prevArrow: '<button type="button" class="slick-nav slick-prev slick-button unset"><svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 24 24" enable-background="new 0 0 24 24" fill="currentColor"><polyline fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" points="17.2,22.4 6.8,12 17.2,1.6 "/></svg></button>',
				nextArrow: '<button type="button" class="slick-nav slick-next slick-button unset"><svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 24 24" enable-background="new 0 0 24 24" fill="currentColor"><polyline fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" points="6.8,22.4 17.2,12 6.8,1.6 "/></svg></button>',
				touchThreshold: 100,
				rows: 0,
				responsive: [
				  {
					breakpoint: 1440,
					settings: {
					  slidesToShow: slider_items_xxl ? slider_items_xxl : (slider_items <= 6 ? slider_items : 5),
					  arrows: slider_arrows_xxl,
					  dots: slider_dots_xxl,
					}
				  }, {
					breakpoint: 1280,
					settings: {
					  slidesToShow: slider_items_xl ? slider_items_xl : (slider_items <= 5 ? slider_items : 4),
					  arrows: slider_arrows_xl,
					  dots: slider_dots_xl,
					}
				  }, {
					breakpoint: 1024,
					settings: {
					  slidesToShow: slider_items_lg ? slider_items_lg : (slider_items <= 4 ? slider_items : 3),
					  arrows: slider_arrows_lg,
					  dots: slider_dots_lg,
					}
				  }, {
					breakpoint: 768,
					settings: {
					  slidesToShow: slider_items_md ? slider_items_md : (slider_items <= 3 ? slider_items : 2),
					  arrows: slider_arrows_md,
					  dots: slider_dots_md,
					}
				  }, {
					breakpoint: 576,
					settings: {
					  slidesToShow: slider_items_sm ? slider_items_sm : (slider_items <= 3 ? slider_items : 2),
					  arrows: slider_arrows_sm,
					  dots: slider_dots_sm,
					}
				  }, {
					breakpoint: 320,
					settings: {
					  slidesToShow: slider_items_xs ? slider_items_xs : (slider_items <= 2 ? slider_items : 1),
					  arrows: slider_arrows_xs,
					  dots: slider_dots_xs,
					}
				  }
				]
			  }

			  $(slider).not('.slick-initialized').slick( args );

			  $(slider).on('setPosition', function(event) {
				let img = $(event.currentTarget).find('.slick-active img');
				let topPosition = img.height()/2;
				topPosition-=$(event.currentTarget).find('.slick-arrow').height()/2;
				$(event.currentTarget).find('.slick-arrow').css('top',topPosition + 'px');
			  }).trigger('afterChange');
			})
		}
	}
	
	/* Countdown */
	function klb_countdown($scope, $) {
		$('.site-countdown').each(function() {
			let $this = $(this);
			let currentDate = $(this).data('date');
			let currentTimeZone = $(this).data('timezone');
			let $days = $this.find('.days');
			let $hours = $this.find('.hours');
			let $minutes = $this.find('.minutes');
			let $second = $this.find('.second');

			let finalDate = moment.tz(currentDate, currentTimeZone);
			$this.countdown(finalDate.toDate(), function(event) {
			  $days.html(event.strftime('%D'));
			  $hours.html(event.strftime('%H'));
			  $minutes.html(event.strftime('%M'));
			  $second.html(event.strftime('%S'));
			});
		});
	}
	
	/* PRODUCT HOVER*/
	function klb_product_hover($scope, $) {
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
	
	
	

    jQuery(window).on('elementor/frontend/init', function () {
		
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-home-slider.default', klb_carousel);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-home-slider2.default', klb_carousel);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-product-carousel.default', klb_carousel);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-banner-carousel.default', klb_carousel);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-testimonial-carousel.default', klb_carousel);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-icon-carousel.default', klb_carousel);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-product-categories.default', klb_carousel);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-product-carousel.default', klb_countdown);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-deals-product.default', klb_countdown);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-deals-product2.default', klb_countdown);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-product-carousel.default', klb_product_hover);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-product-list.default', klb_product_hover);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-deals-product.default', klb_product_hover);
		elementorFrontend.hooks.addAction('frontend/element_ready/bumedi-deals-product2.default', klb_product_hover);
		
    });

})(jQuery);
