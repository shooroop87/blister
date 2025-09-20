(function ($) {
  "use strict";

	$(document).on('bumediShopPageInit', function () {
		bumediThemeModule.countdown();
	});

	bumediThemeModule.countdown = function() {
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
	
	$(document).ready(function() {
		bumediThemeModule.countdown();
	});

})(jQuery);
