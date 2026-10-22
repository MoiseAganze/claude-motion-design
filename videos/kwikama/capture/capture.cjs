// Real-state 4K captures of https://kwikama.vercel.app (viewport 1920×1080 @2x).
// usage: NODE_PATH=<playwright> node capture/capture.cjs [scene...]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const BASE = 'https://kwikama.vercel.app';
const OUT = path.join(__dirname);
const only = process.argv.slice(2);
const boxes = {};

async function setup() {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 2 });
  const p = await ctx.newPage();
  return { b, p };
}
async function login(p, fil, role) {
  await p.goto(BASE + '/connexion', { waitUntil: 'networkidle' });
  await p.getByRole('button', { name: new RegExp('Procédure ' + fil) }).click();
  await p.getByRole('button', { name: new RegExp(role) }).first().click();
  await p.waitForURL('**/app**');
  await p.waitForTimeout(900);
}
async function nav(p, href) {
  await p.click(`nav a[href="${href}"]`);
  await p.waitForLoadState('networkidle');
  await p.waitForTimeout(1200);
}
async function box(p, scene, key, locator) {
  const bb = await locator.boundingBox();
  if (!bb) throw new Error(`no box for ${scene}/${key}`);
  (boxes[scene] ||= {})[key] = { x: Math.round(bb.x), y: Math.round(bb.y), w: Math.round(bb.width), h: Math.round(bb.height) };
}
async function shot(p, scene, name, opts = {}) {
  const dir = path.join(OUT, scene);
  fs.mkdirSync(dir, { recursive: true });
  await p.waitForTimeout(opts.wait ?? 500);
  await p.screenshot({ path: path.join(dir, name + '.png'), ...opts.ss });
}
// Tall strip of the page: grow the viewport so the whole document lays out, screenshot, restore.
async function tall(p, scene, name) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  await p.setViewportSize({ width: 1920, height: h });
  await p.waitForTimeout(700);
  await shot(p, scene, name, { wait: 200 });
  await p.setViewportSize({ width: 1920, height: 1080 });
  await p.waitForTimeout(400);
  (boxes[scene] ||= {})[name + '_height'] = h;
  return h;
}
const scrollTo = async (p, y) => { await p.evaluate(y => window.scrollTo(0, y), y); await p.waitForTimeout(700); };
const topOf = (p, loc) => loc.evaluate(e => e.getBoundingClientRect().top + window.scrollY);

const scenes = {
  async f02(p) {
    await p.goto(BASE + '/', { waitUntil: 'networkidle' });
    await p.waitForTimeout(1500);
    await shot(p, 'f02', 'hero');
    const net = p.getByText('Dix-huit institutions, reliées');
    const y = await topOf(p, net);
    await scrollTo(p, y - 260);
    await p.waitForTimeout(4000);
    await shot(p, 'f02', 'network');
    const aplc = p.locator('svg text, button').filter({ hasText: /^APLC$/ }).first();
    await box(p, 'f02', 'aplc', aplc);
    await aplc.click({ force: true });
    await p.waitForTimeout(1200);
    (boxes.f02 ||= {}).scrollAfterClick = await p.evaluate(() => window.scrollY);
    await shot(p, 'f02', 'network-aplc');
    const panel = p.getByText("Agence de Prévention et de Lutte contre la Corruption").first();
    await box(p, 'f02', 'aplcPanel', panel.locator('xpath=..'));
    const per = p.getByText('Deux périmètres à ne pas confondre');
    await scrollTo(p, (await topOf(p, per)) - 300);
    await shot(p, 'f02', 'perimetres');
    for (const [k, t] of [['plateforme', 'La plateforme'], ['laboratoire', 'Le laboratoire']]) {
      const card = p.getByText(t, { exact: true }).first().locator('xpath=ancestor::*[self::article or self::div][1]');
      await box(p, 'f02', k, card);
    }
  },

  async f03(p) {
    await p.goto(BASE + '/connexion', { waitUntil: 'networkidle' });
    const card = p.getByRole('button', { name: /Procédure UNICEP/ });
    await scrollTo(p, (await topOf(p, card)) - 140);
    await box(p, 'f03', 'unicep', card);
    await box(p, 'f03', 'aplc', p.getByRole('button', { name: /Procédure APLC/ }));
    await card.click();
    await shot(p, 'f03', 'unicep');
    await p.getByRole('button', { name: /Procédure APLC/ }).click();
    await shot(p, 'f03', 'aplc', { wait: 900 });
    await p.getByRole('button', { name: /Procédure UNICEP/ }).click();
    await shot(p, 'f03', 'unicep-again', { wait: 900 });
    await login(p, 'UNICEP', 'Point focal');
    await shot(p, 'f03', 'dash-pointfocal');
    await login(p, 'UNICEP', 'Coordonnateur UNICEP');
    await shot(p, 'f03', 'dash-coord');
    const items = await p.locator('nav a').evaluateAll(as => as.map(a => { const r = a.getBoundingClientRect(); return { href: a.getAttribute('href'), text: a.textContent.trim(), y: Math.round(r.y), h: Math.round(r.height) }; }));
    (boxes.f03 ||= {}).navCoord = items;
  },

  async f04(p) {
    await login(p, 'UNICEP', 'Coordonnateur UNICEP');
    await nav(p, '/app/verification');
    await shot(p, 'f04', 'list');
    await box(p, 'f04', 'callout', p.getByText('Propre à la filière UNICEP.').first().locator('xpath=..'));
    await scrollTo(p, 100000);
    (boxes.f04 ||= {}).scroll = await p.evaluate(() => window.scrollY);
    await shot(p, 'f04', 'list-bottom');
    const row = p.getByText('SIG-2026-0195');
    await box(p, 'f04', 'row', row);
    await box(p, 'f04', 'rowCard', row.locator('xpath=ancestor::button[1]'));
    await row.click();
    await shot(p, 'f04', 'panel-0', { wait: 1000 });
    const panel = p.locator('[role=dialog], aside').filter({ has: p.getByText('Contrôles du manuel') }).last();
    const radios = p.locator('input[type=radio]');
    const picks = [0, 2, 5, 6];
    await radios.nth(0).scrollIntoViewIfNeeded();
    await shot(p, 'f04', 'panel-controls-0');
    for (const [i, r] of picks.entries()) {
      const label = radios.nth(r).locator('xpath=..');
      await box(p, 'f04', 'pick' + i, label);
      await radios.nth(r).check({ force: true });
      await shot(p, 'f04', 'panel-controls-' + (i + 1), { wait: 400 });
    }
    const btn = p.getByRole('button', { name: 'Valider la régularité' });
    await box(p, 'f04', 'valider', btn);
    await btn.click();
    await shot(p, 'f04', 'validated', { wait: 1200 });
    await box(p, 'f04', 'rowCardDone', p.getByText('SIG-2026-0195').locator('xpath=ancestor::button[1]'));
    await box(p, 'f04', 'session', p.getByText(/Actions de cette session/i).first().locator('xpath=..'));
    await nav(p, '/app/dossiers');
    await shot(p, 'f04', 'registre');
    await box(p, 'f04', 'numCol', p.locator('table').first());
    await box(p, 'f04', 'session2', p.getByText(/Actions de cette session/i).first().locator('xpath=..'));
  },

  async f05(p) {
    await login(p, 'UNICEP', 'Coordonnateur UNICEP');
    await nav(p, '/app/passerelles');
    await shot(p, 'f05', 'top');
    await tall(p, 'f05', 'tall');
    for (const [k, t] of [['tofo', 'Plateforme nationale de transparence des marchés publics'], ['itie', 'Initiative pour la Transparence des Industries Extractives'], ['guce', 'Guichet Unique de Création'], ['guceLine', "L'identité des personnes physiques"], ['kpi', 'REGISTRES RACCORDÉS'], ['simu', 'Architecture simulée']]) {
      const el = p.getByText(t, { exact: false }).first();
      const card = ['tofo', 'itie', 'guce'].includes(k) ? el.locator('xpath=ancestor::article[1] | ancestor::section[1]').last() : (k === 'kpi' ? el.locator('xpath=..') : el);
      const bb = await (await card.count() ? card : el).evaluate(e => { const r = e.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y + window.scrollY), w: Math.round(r.width), h: Math.round(r.height) }; });
      (boxes.f05 ||= {})['doc_' + k] = bb;
    }
    const guce = p.getByText('Guichet Unique de Création', { exact: false }).first();
    await scrollTo(p, (await topOf(p, guce)) - 420);
    await shot(p, 'f05', 'registres');
    await box(p, 'f05', 'guce', guce);
    await nav(p, '/app/avoirs');
    await p.getByText('AVR-2026-072').first().click();
    await p.waitForTimeout(1000);
    await shot(p, 'f05', 'beneficiaire');
    for (const [k, re] of [['proprio', /Propriétaire déclaré/i], ['be', /Bénéficiaire effectif/i]]) {
      const dt = p.locator('dt:visible').filter({ hasText: re }).first();
      await box(p, 'f05', k + '_dt', dt);
      await box(p, 'f05', k + '_dd', dt.locator('xpath=following-sibling::dd[1]'));
    }
  },

  async f06(p) {
    await login(p, 'UNICEP', 'Coordonnateur UNICEP');
    await nav(p, '/app/dossiers');
    await p.getByText('DPJ-2026-014').first().click();
    await p.waitForTimeout(1500);
    await shot(p, 'f06', 'dossier');
    await tall(p, 'f06', 'chronologie-tall');
    const tab = n => p.locator('main button', { hasText: new RegExp('^' + n + '$') }).first();
    await box(p, 'f06', 'tabPreuves', tab('Preuves'));
    await tab('Preuves').click();
    await p.waitForTimeout(1200);
    await shot(p, 'f06', 'preuves');
    await tall(p, 'f06', 'preuves-tall');
    await nav(p, '/app/enquete-financiere');
    await p.locator('main select').first().selectOption({ label: 'DPJ-2026-014' }).catch(() => {});
    await p.waitForTimeout(2500);
    await shot(p, 'f06', 'graphe');
    const node = await p.evaluate(() => { const c = [...document.querySelectorAll('main svg circle')].find(c => /Ilunga/.test(c.closest('g')?.textContent || '')); const r = c.getBoundingClientRect(); return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) }; });
    (boxes.f06 ||= {}).node = node;
    await p.mouse.move(node.x, node.y); await p.mouse.down(); await p.mouse.up();
    await shot(p, 'f06', 'graphe-select', { wait: 1500 });
  },

  async f07(p) {
    await login(p, 'UNICEP', 'Coordonnateur UNICEP');
    await nav(p, '/app/analyse');
    await shot(p, 'f07', 'before');
    const btn = p.getByRole('button', { name: "Lancer l'analyse" }).first();
    await box(p, 'f07', 'lancer', btn);
    await btn.click();
    for (let i = 0; i < 16; i++) { await p.screenshot({ path: path.join(OUT, 'f07', `run-${String(i).padStart(2, '0')}.png`) }); await p.waitForTimeout(120); }
    await p.getByText('Ce que l\'analyse n\'a pas pu établir').waitFor();
    await p.waitForTimeout(800);
    await shot(p, 'f07', 'result');
    const h = await tall(p, 'f07', 'result-tall');
    for (const [k, t] of [['rapprochement', 'Rapprochements proposés'], ['signaux', 'Signaux relevés sur les pièces'], ['angles', "Ce que l'analyse n'a pas pu établir"], ['decisions', 'DÉCISIONS ENREGISTRÉES']]) {
      (boxes.f07 ||= {})['y_' + k] = Math.round(await topOf(p, p.getByText(t, { exact: false }).first()));
    }
    const ret = p.getByRole('button', { name: /Retenir la piste/ }).first();
    await ret.scrollIntoViewIfNeeded();
    await p.waitForTimeout(600);
    (boxes.f07 ||= {}).scroll_retenir = await p.evaluate(() => window.scrollY);
    await box(p, 'f07', 'retenir', ret);
    await shot(p, 'f07', 'retenir-before');
    await ret.click();
    await shot(p, 'f07', 'retenir-after', { wait: 1000 });
    await scrollTo(p, 0);
    await shot(p, 'f07', 'counter-after');
    await tall(p, 'f07', 'result-tall-after');
  },

  async f08(p) {
    await login(p, 'UNICEP', 'Coordonnateur UNICEP');
    await nav(p, '/app/coordination');
    await shot(p, 'f08', 'top');
    await tall(p, 'f08', 'tall');
    const docBox = (loc) => loc.evaluate(e => { const r = e.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y + scrollY), w: Math.round(r.width), h: Math.round(r.height) }; });
    for (const [k, t] of [['d48', "Notification au parquet de l'ouverture"], ['d7', 'Réquisition d\'informations (banques'], ['d72', 'Suivi des mesures coercitives']]) {
      (boxes.f08 ||= {})['doc_' + k] = await docBox(p.getByText(t, { exact: false }).last().locator('xpath=ancestor::tr[1]'));
    }
    const row = p.getByText('RQ-2026-0091').first();
    (boxes.f08 ||= {}).doc_row = await docBox(row.locator('xpath=ancestor::tr[1]'));
    await scrollTo(p, (await topOf(p, row)) - 520);
    (boxes.f08 ||= {}).tableScroll = await p.evaluate(() => window.scrollY);
    await shot(p, 'f08', 'table');
    await box(p, 'f08', 'row', row);
    await row.click();
    await shot(p, 'f08', 'panel', { wait: 1000 });
    const rel = p.getByRole('button', { name: 'Émettre une relance' });
    await box(p, 'f08', 'relance', rel);
    await rel.click();
    await shot(p, 'f08', 'relancee', { wait: 1200 });
    await p.getByRole('button', { name: 'Fermer le panneau de détail' }).click().catch(() => {});
    await shot(p, 'f08', 'table-after', { wait: 800 });
    await login(p, 'UNICEP', 'Administrateur');
    await nav(p, '/app/administration');
    await p.getByText("Journal d'audit", { exact: true }).first().click();
    await p.waitForTimeout(1000);
    const line = p.getByText('RQ-2026-0091').first();
    await scrollTo(p, (await topOf(p, line)) - 560);
    await shot(p, 'f08', 'journal');
    await box(p, 'f08', 'line', line.locator('xpath=ancestor::tr'));
    await box(p, 'f08', 'lineRelance', p.getByText("Relance d'une réquisition en retard").first().locator('xpath=ancestor::tr'));
  },

  async f09(p) {
    await login(p, 'UNICEP', 'Coordonnateur UNICEP');
    await nav(p, '/app/dossiers');
    await p.getByText('DPJ-2026-014').first().click();
    await p.waitForTimeout(1500);
    const rt = p.getByText('Revue technique du superviseur').first();
    await scrollTo(p, (await topOf(p, rt)) - 200);
    await shot(p, 'f09', 'qualite');
    for (const [k, t] of [['rt', 'Revue technique du superviseur'], ['rj', 'Revue juridique et conformité'], ['cie', "Comité interne d'examen"], ['tr', "Transmission à l'autorité compétente"], ['ar', 'Accusé de réception']]) {
      await box(p, 'f09', k, p.getByText(t, { exact: false }).first());
    }
    (boxes.f09 ||= {}).scroll = await p.evaluate(() => window.scrollY);
  },

  async f10(p) {
    await login(p, 'UNICEP', 'Coordonnateur UNICEP');
    await nav(p, '/app/avoirs');
    await shot(p, 'f10', 'encart');
    await tall(p, 'f10', 'tall');
    const docBox = (loc) => loc.evaluate(e => { const r = e.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y + scrollY), w: Math.round(r.width), h: Math.round(r.height) }; });
    const B = (boxes.f10 = {});
    for (const k of ['Identifiés', 'Gelés', 'Saisis', 'Confisqués ou restitués']) B['doc_' + k] = await docBox(p.getByText(new RegExp('^' + k + '$', 'i')).first().locator('xpath=..'));
    B.doc_quote = await docBox(p.getByText("Une enquête qui ne récupère rien n'a rien réparé.").first());
    B.doc_row = await docBox(p.getByText('AVR-2026-072').first().locator('xpath=ancestor::tr[1]'));
    await scrollTo(p, 300);
    B.S = await p.evaluate(() => window.scrollY);
    await shot(p, 'f10', 'listS');
    await p.getByText('AVR-2026-072').first().click();
    await p.waitForTimeout(1000);
    B.scrollPanel = await p.evaluate(() => window.scrollY);
    await shot(p, 'f10', 'panel-gele');
    const btn = p.getByRole('button', { name: /Passer au statut « Saisi »/ });
    await box(p, 'f10', 'saisir', btn);
    await btn.click();
    await shot(p, 'f10', 'panel-saisi', { wait: 1200 });
    await p.getByRole('button', { name: 'Fermer le panneau de détail' }).click().catch(() => {});
    await p.waitForTimeout(800);
    await scrollTo(p, B.S);
    await shot(p, 'f10', 'listS-after');
    await box(p, 'f10', 'session', p.getByText(/Actions de cette session/i).first().locator('xpath=..'));
    await scrollTo(p, 0);
    await shot(p, 'f10', 'encart-after');
    await tall(p, 'f10', 'tall-after');
  },
};

(async () => {
  const { b, p } = await setup();
  for (const [name, fn] of Object.entries(scenes)) {
    if (only.length && !only.includes(name)) continue;
    const t0 = Date.now();
    try { await fn(p); console.log(`✓ ${name} ${((Date.now() - t0) / 1000).toFixed(1)}s`); }
    catch (e) { console.log(`✗ ${name}: ${e.message.split('\n')[0]}`); }
  }
  const bf = path.join(OUT, 'boxes.json');
  const prev = fs.existsSync(bf) ? JSON.parse(fs.readFileSync(bf, 'utf8')) : {};
  fs.writeFileSync(bf, JSON.stringify({ ...prev, ...boxes }, null, 1));
  await b.close();
})();
