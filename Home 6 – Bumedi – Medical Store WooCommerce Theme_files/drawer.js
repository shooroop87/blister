(function ($) {
  "use strict";
  
  const drawers = gsap.utils.toArray(document.querySelectorAll('.site-drawer'));
  const buttons = document.querySelectorAll([".menu-toggle a", ".cart-toggle a", ".search-toggle a", ".categories-toggle a"]);
  let activeAnimation = gsap.to({}, {});

  const removeButtonClass = () => {
    if (buttons !== null) {
      buttons.forEach((button) => {
        button.classList.remove('active');
      });
    }
  }

  const buttonClicked = (button, anim) => {
    document.body.classList.remove('site-drawer-active');
    removeButtonClass();

    activeAnimation.reverse();
    activeAnimation = anim;
    if (!activeAnimation.isActive()) {
      activeAnimation.play();
      button.classList.add('active');
      document.body.classList.toggle('site-drawer-active');
    }
  }

  if (buttons !== null) {
    buttons.forEach((button) => {
      let clickedButton = null;
      if (button.closest("LI, .site-header-action-mobile").classList.contains("menu-toggle")) {
        clickedButton = "menu-toggle-holder";
      } else if (button.closest("LI, .site-header-action-mobile").classList.contains("cart-toggle")) {
        clickedButton = "cart-toggle-holder";
      } else if (button.closest("LI, .site-header-action-mobile").classList.contains("search-toggle")) {
        clickedButton = "search-toggle-holder";
      } else {
        clickedButton = "categories-toggle-holder";
      }

      const currentDrawer = drawers.filter(x => x.id === clickedButton)[0];
      let tl = gsap.timeline({ paused: true, reversed: true });

      if (currentDrawer !== null) {
        const drawerInner = currentDrawer.querySelector('.site-drawer-inner');
        const drawerOverlay = currentDrawer.querySelector('.site-drawer-overlay');

        tl.to(currentDrawer, .1, {
          autoAlpha: 1
        }).to(drawerOverlay, .2, {
          autoAlpha: 1
        }, "-=.1").to(drawerInner, .5, {
          x: 0,
          y: 0,
          autoAlpha: 1,
          ease: 'power4.inOut'
        }, "-=.35")
      }

      button.addEventListener("click", (e) => {
        e.preventDefault();

        const currentButton = e.target.closest('A');
        currentButton.anim = tl;
        buttonClicked(currentButton, currentButton.anim);
      })
    })
  }

  if (drawers !== null) {
    for( var i = 0; i < drawers.length; i++ ) {
      const self = drawers[i];
      const drawerClose = self.querySelector('.site-close a');

      if (drawerClose !== null) {
        drawerClose.addEventListener('click', (e) => {
          e.preventDefault();
          document.body.classList.remove('site-drawer-active');
          removeButtonClass();
          activeAnimation.reverse(1);
        })
      }
    }
  }


}(jQuery));