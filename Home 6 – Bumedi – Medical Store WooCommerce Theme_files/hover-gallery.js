class HoverGallery {
  constructor(option) {
    this.selector = option.selector ? option.selector : ".klb-hover-gallery";
    this.slideDuration = option.duration ? option.duration : 0.3;
    this.resetHover = option.resetHover;
    this.style = option.style;
    this.slides = gsap.utils.toArray(this.selector.children);
    this.slidesLength = this.slides.length;
    this.selectorWrapper = document.createElement('DIV');
    this.selectorInner = document.createElement('DIV');
    this.progressPerItem = 1 / (this.slidesLength - 1);
    this.threshold = this.progressPerItem / 5;
    this.snapProgress = gsap.utils.snap(this.progressPerItem)
    this.slideWidth = 0;
    this.totalWidth = 0;
    this.currentIndex = 0;

    this.animation = gsap.to(this.slides, 1, {
      xPercent: "-=" + (this.slidesLength - 1) * 100,
      ease: "none",
      paused: true
    })

    this.init( () => {
      if (this.style === "hover") {
        this.createHoverBlocks();
      }
    });
  }

  // Init gallery
  init(el) {
    const promises = [];
    const { selector, slides, slidesLength, selectorWrapper, selectorInner } = this;

    if (slidesLength > 1) {
      slides[0].classList.add('active');
      selector.classList.add('klb-hover-gallery');

      const wrap = (el, wrapper, classNames = null, dots = false) => {
        el.parentNode.insertBefore(wrapper, el);
        if (classNames !== null) {
          wrapper.classList.add(classNames);
        }
        wrapper.appendChild(el);
        if (dots) {
          this.createNavigations();
        }
      }

      wrap(selector, selectorInner, 'klb-hover-gallery-inner', false);
      wrap(selectorInner, selectorWrapper, 'klb-hover-gallery-wrapper', true);
    }

    Promise.all( promises ).then( () => {
      el();
    });
  }

  // Create gallery navigations
  createNavigations() {
    const { slides, selectorWrapper } = this;
    // Create dots wrapper
    let dotsFragment = document.createDocumentFragment();
    let arrowsFragment = document.createDocumentFragment();
    const dotsWrapper = document.createElement('DIV');
    const arrowsWrapper = document.createElement('DIV');
    dotsWrapper.classList.add('klb-hover-gallery-dots');
    arrowsWrapper.classList.add('klb-hover-gallery-arrows');

    // Create dots
    for (var i = 0; i < slides.length; i++) {
      let dot = dotsWrapper.appendChild(document.createElement('DIV'));
      dot.classList.add('dot');
      selectorWrapper.appendChild(dotsWrapper);
    }

    // Create arrows
    let arrowPrev = arrowsWrapper.appendChild(document.createElement('DIV'));
    let arrowNext = arrowsWrapper.appendChild(document.createElement('DIV'));
    const prevSVG = `<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 24 24" enable-background="new 0 0 24 24" fill="currentColor"><polyline fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" points="17.2,22.4 6.8,12 17.2,1.6 "/></svg>`;
    const nextSVG = `<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 24 24" enable-background="new 0 0 24 24" fill="currentColor"><polyline fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" points="6.8,22.4 17.2,12 6.8,1.6 "/></svg>`;
    arrowPrev.classList.add('klb-hover-gallery-nav', 'prev', 'disable');
    arrowNext.classList.add('klb-hover-gallery-nav', 'next');
    arrowPrev.innerHTML = prevSVG;
    arrowNext.innerHTML = nextSVG;
    selectorWrapper.appendChild(arrowsWrapper);

    if (!dotsFragment) {
      selectorWrapper.appendChild(dotsFragment);
    }

    if (!arrowsFragment) {
      selectorWrapper.appendChild(arrowsFragment);
    }

    dotsWrapper.querySelectorAll(':scope > *')[0].classList.add('active');
    arrowPrev.addEventListener('click', (e) => {
      e.preventDefault();
      this.animationSlides(-1);
      if (this.currentIndex === 0) {
        e.target.closest('DIV').classList.add('disable')
      }
      if (arrowNext.classList.contains('disable')) {
        arrowNext.classList.remove('disable');
      }
    });
    arrowNext.addEventListener('click', (e) => {
      e.preventDefault();
      this.animationSlides(1);
      arrowPrev.classList.remove('disable');
      if ((this.slidesLength - 1) === this.currentIndex) {
        e.target.closest('DIV').classList.add('disable')
      }
    });
  }

  // Change active class
  changeActiveClass(index) {
    const dots = this.selectorWrapper.querySelectorAll('.klb-hover-gallery-dots .dot');
    
    [...dots, ...this.slides].forEach((item) => {
      item.classList.remove('active');
    })
    
    dots[index].classList.add('active');
    this.slides[index].classList.add('active');
  }

  // Animation slides
  animationSlides(direction) {
    let progress = this.snapProgress(
      this.animation.progress() + direction * this.progressPerItem
    );

    if (direction === 1) {
      if ((this.slidesLength - 1) === this.currentIndex) {
        return;
      }
      this.currentIndex += 1;
    } else {
      if (this.currentIndex === 0) {
        return;
      }
      this.currentIndex -= 1;
    }

    if (progress >= 0 && progress <= 1) {
      gsap.to(this.animation, {
        progress: progress,
        duration: this.slideDuration,
        overwrite: true,
      });
    }
  }

  // Hover gallery blocks for desktop
  createHoverBlocks() {
    const { slides, slidesLength, selectorWrapper } = this;
    if (slidesLength > 1) {
      // Create hover gallery wrapper
      let blockFragment = document.createDocumentFragment();
      const hoverGalleryWrapper = document.createElement('DIV');
      hoverGalleryWrapper.classList.add('klb-hover-gallery-hover');

      // Create dots
      for (var i = 0; i < slides.length; i++) {
        let block = hoverGalleryWrapper.appendChild(document.createElement('DIV'));
        block.classList.add('klb-hover-block');
        selectorWrapper.appendChild(hoverGalleryWrapper);
      }

      if (!blockFragment) {
        selectorWrapper.appendChild(blockFragment);
      }

      hoverGalleryWrapper.querySelectorAll(':scope > *')[this.currentIndex].classList.add('active');
      this.slideHoverBlocks(hoverGalleryWrapper);
    }
  }

  slideHoverBlocks(wrapper) {
    const blocks = wrapper.querySelectorAll('.klb-hover-gallery-hover .klb-hover-block');

    const removeClass = () => {
      blocks.forEach((block) => {
        block.classList.remove('active');
      })
    }

    const over = (e) => {
      this.currentIndex = Array.prototype.slice.call(wrapper.children).indexOf( e.target );
      removeClass();
      e.target.classList.add('active');
      this.changeActiveClass(this.currentIndex);
    }

    const leave = (e) => {
      this.currentIndex = this.currentIndex;
      removeClass();
      wrapper.children[0].classList.add('active');
      this.changeActiveClass(this.resetHover ? 0 : this.currentIndex);
    }

    wrapper.addEventListener('mouseover', (e) => {
      over(e);
    })

    wrapper.addEventListener('mouseleave', (e) => {
      leave(e);
    })
  }
}