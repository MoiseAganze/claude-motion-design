// Shared helpers for the captured-screen scenes. Screen coordinates are the prototype's CSS px (1920×1080 viewport).
// Every helper only adds tweens to the scene's paused timeline: seek-safe, deterministic.
window.KIT = (function () {
  const CURSOR = '<svg viewBox="0 0 24 32" width="30" height="40"><path d="M2 2 L2 26 L8.2 20.4 L12.4 30 L16.6 28.2 L12.6 18.8 L21 18.8 Z" fill="#FFFFFF" stroke="#031829" stroke-width="1.8" stroke-linejoin="round"/></svg>';

  // camera transform that puts screen point (fx, fy) at the frame centre at scale s, clamped so no edge shows
  function cam(fx, fy, s) {
    s = Math.max(1, s);
    const x = Math.min(0, Math.max(1920 - 1920 * s, 960 - fx * s));
    const y = Math.min(0, Math.max(1080 - 1080 * s, 540 - fy * s));
    return { x, y, scale: s };
  }

  function mount(root, prefix) {
    const c = document.createElement("div");
    c.id = prefix + "-cursor"; c.className = "kit-cursor"; c.innerHTML = CURSOR;
    c.style.cssText = "position:absolute;left:0;top:0;width:30px;height:40px;transform-origin:3px 3px;";
    const r = document.createElement("div");
    r.id = prefix + "-ring"; r.className = "kit-ring";
    r.style.cssText = "position:absolute;left:-22px;top:-22px;width:44px;height:44px;border:3px solid #D8A828;border-radius:50%;opacity:0;";
    root.appendChild(r); root.appendChild(c);
    return { cursor: c, ring: r };
  }

  // Scrolling page: the viewport shot stays as the sticky chrome (banner, sidebar, header), a full-height shot of the
  // same page slides under it in the content window. Marks placed in `layer` use document coordinates.
  function page(parent, id, viewportSrc, tallSrc, tallH, top = 101, left = 256) {
    parent.insertAdjacentHTML("beforeend",
      `<img id="${id}-base" src="${viewportSrc}" alt="" style="position:absolute;left:0;top:0;width:1920px;height:1080px;" />` +
      `<div id="${id}-win" style="position:absolute;left:${left}px;top:${top}px;width:${1920 - left}px;height:${1080 - top}px;overflow:hidden;">` +
      `<div id="${id}-scroll" style="position:absolute;left:${-left}px;top:${-top}px;width:1920px;height:${tallH}px;">` +
      `<img src="${tallSrc}" alt="" style="position:absolute;left:0;top:0;width:1920px;height:${tallH}px;" /><div id="${id}-layer"></div></div></div>`);
    return { base: parent.querySelector("#" + id + "-base"), scroll: parent.querySelector("#" + id + "-scroll"), layer: parent.querySelector("#" + id + "-layer"), win: parent.querySelector("#" + id + "-win") };
  }

  return {
    cam,
    mount,
    page,
    scrollTo(tl, pg, y, t, d = 1.0) { tl.to(pg.scroll, { y: -y, duration: d, ease: "power2.inOut" }, t); },
    // first appearance of the cursor
    cursorAt(tl, k, x, y, t) {
      tl.fromTo(k.cursor, { x, y, opacity: 0, scale: 1 }, { x, y, opacity: 1, scale: 1, duration: 0.3, ease: "power1.out" }, t);
    },
    move(tl, k, x, y, t, d = 0.9) {
      tl.to(k.cursor, { x, y, duration: d, ease: "power2.inOut" }, t);
    },
    // press + gold ring; the caller holds ≥1.5 s before the next move
    click(tl, k, x, y, t) {
      tl.to(k.cursor, { scale: 0.86, duration: 0.08, ease: "power1.in" }, t);
      tl.to(k.cursor, { scale: 1, duration: 0.16, ease: "power2.out" }, t + 0.08);
      tl.set(k.ring, { x, y }, t);
      tl.fromTo(k.ring, { opacity: 0.95, scale: 0.4 }, { opacity: 0, scale: 1.25, duration: 0.6, ease: "power2.out", immediateRender: false }, t);
    },
    hide(tl, k, t) { tl.to(k.cursor, { opacity: 0, duration: 0.3, ease: "power1.in" }, t); },
    show(tl, el, t, d = 0.5) { tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: d, ease: "power1.inOut", immediateRender: false }, t); },
    hideEl(tl, el, t, d = 0.5) { tl.to(el, { opacity: 0, duration: d, ease: "power1.inOut" }, t); },
    camTo(tl, el, fx, fy, s, t, d = 1.2) { tl.to(el, { ...cam(fx, fy, s), duration: d, ease: "power2.inOut" }, t); },
    // gold outline around a screen box, in and out
    mark(tl, el, t, hold, d = 0.35) {
      tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: d, ease: "power2.out", immediateRender: false }, t);
      if (hold != null) tl.to(el, { opacity: 0, duration: 0.5, ease: "power1.inOut" }, t + hold);
    },
    box(id, b, pad = 8) {
      const e = document.createElement("div");
      e.id = id; e.className = "kit-mark";
      e.style.cssText = `position:absolute;left:${b.x - pad}px;top:${b.y - pad}px;width:${b.w + 2 * pad}px;height:${b.h + 2 * pad}px;border:3px solid #D8A828;border-radius:8px;opacity:0;`;
      return e;
    },
  };
})();
