(function ($) {
  "use strict";

  const menuDrawer = document.querySelectorAll('.site-menu-drawer');

  if (menuDrawer !== null) {
    for( var i = 0; i < menuDrawer.length; i++ ) {
      const self = menuDrawer[i];
      const hasChildren = self.querySelectorAll( '.menu-item-has-children' );
      const subMenu = ( e ) => {
        let subUl;
        if ( e.target.tagName === 'A' ) {
          e.preventDefault();
          subUl = e.target.nextElementSibling;
        } else {
          subUl = e.target.previousElementSibling;
        }
        let parentUl = e.target.closest( 'ul' );
        let parentLi = e.target.closest( 'li' );
        let activeLi = parentUl.querySelectorAll( '.menu-item-has-children.active' );

        const closeSubs = () => {
          for ( var i = 0; i < activeLi.length; i++ ) {
            const activeSub = activeLi[i].children[1];
            const childSubs = activeSub.querySelectorAll( '.sub-menu' );
            for ( var i = 0; i < childSubs.length; i++ ) {
              if ( childSubs[i] != null ) {
                gsap.set( childSubs[i], { height: 0 } );
              }
            }
          }
        }

        const subAnimation = ( element, event ) => {
          gsap.to( element, { duration: .4, height: event, ease: 'power4.inOut', onComplete: closeSubs } );
        }

        if ( !parentLi.classList.contains( 'active' ) ) {
          for ( var i = 0; i < activeLi.length; i++ ) {
            activeLi[i].classList.remove( 'active' );
            const sub = activeLi[i].children[1];
            subAnimation( sub, 0 );
          }
          parentLi.classList.add( 'active' );
          subAnimation( subUl, 'auto' );
        } else {
          parentLi.classList.remove( 'active' );
          subAnimation( subUl, 0 );
        }

      }
	  if (hasChildren.length !== 0) {
		  for( var i = 0; i < hasChildren.length; i++ ) {
			const dropdown = document.createElement( 'span' );
			dropdown.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-down"><polyline points="6 9 12 15 18 9"></polyline></svg>';
			dropdown.className = 'menu-dropdown';
			hasChildren[i].appendChild( dropdown );

			const link = hasChildren[i].querySelector( 'a[href*="#"]' );
			const sub = hasChildren[i].children[1];
			gsap.set( sub, { height: 0 } );
			dropdown.addEventListener( 'click', subMenu );
			if (link !== null) {
				link.addEventListener( 'click', subMenu );
			}
		  }
	  }
    }
  }

}(jQuery));