#!/usr/bin/env python3
"""
Regenerates reader.html from index.json + all source files.
Run after adding new sources: python build_reader.py
"""

import argparse
import json, os, sys


def render(base):
    """Return rendered HTML and any index entries whose files are missing."""
    with open(os.path.join(base, "index.json"), encoding="utf-8") as f:
        index = json.load(f)

    sources, skipped = [], []
    for entry in index["sources"]:
        path = os.path.join(base, entry["file"])
        if not os.path.exists(path):
            skipped.append(entry["file"])
            continue
        with open(path, encoding="utf-8") as f:
            src = json.load(f)
        src["title_short"] = entry["title_short"]
        sources.append(src)

    for s in skipped:
        print(f"skip (not found): {s}", file=sys.stderr)

    data_json = json.dumps(sources, ensure_ascii=False, separators=(",", ":"))
    data_json = data_json.replace("</", "<\\/")   # prevent </script> injection

    return TEMPLATE.replace("__SOURCES_JSON__", data_json), skipped, len(sources)


def main():
    parser = argparse.ArgumentParser(description="Build or check the generated source-library reader.")
    parser.add_argument("--check", action="store_true", help="Fail if reader.html is stale; do not write it.")
    args = parser.parse_args()
    base = os.path.dirname(os.path.abspath(__file__))
    rendered, skipped, count = render(base)

    out = os.path.join(base, "reader.html")
    if args.check:
        current = ""
        if os.path.exists(out):
            with open(out, encoding="utf-8") as f:
                current = f.read()
        if skipped or current != rendered:
            print("reader.html is stale; run `python scripts/literature.py fix`.", file=sys.stderr)
            raise SystemExit(1)
        print(f"reader.html is current ({count} sources)")
        return

    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(rendered)

    print(f"reader.html  ({count} sources, {os.path.getsize(out):,} bytes)")


# ---------------------------------------------------------------------------
# HTML template — __SOURCES_JSON__ is replaced at build time
# ---------------------------------------------------------------------------
TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>MCS SIG AI/ML — Source Library</title>
<style>
:root {
  --bg:      #f9fafb;
  --surface: #ffffff;
  --border:  #e5e7eb;
  --text:    #111827;
  --muted:   #6b7280;
  --hover:   #f3f4f6;
  --sel-bg:  #eff6ff;
  --sel-bar: #2563eb;
  --list-w:  400px;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 14px;
  background: var(--bg);
  color: var(--text);
  height: 100vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

/* ── Filter bar ─────────────────────────────── */
#filters {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 8px 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex-shrink: 0;
}
.frow {
  display: flex;
  align-items: center;
  gap: 5px;
  flex-wrap: wrap;
}
.flabel {
  font-size: 10px;
  font-weight: 700;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .07em;
  min-width: 46px;
  flex-shrink: 0;
}
.fsep { flex: 1; min-width: 10px; }
.chip {
  border: 1.5px solid var(--border);
  background: var(--surface);
  border-radius: 999px;
  padding: 3px 11px;
  font-size: 12px;
  cursor: pointer;
  white-space: nowrap;
  color: var(--text);
  font-family: inherit;
  transition: background .1s, border-color .1s, color .1s;
}
.chip:hover { background: var(--hover); }
.chip.active { background: #374151; border-color: #374151; color: #fff; }

.sort-group {
  display: flex;
  align-items: center;
  gap: 5px;
  width: 100%;
  white-space: nowrap;
}
#sort-key, #sort-direction {
  border: 1.5px solid var(--border);
  background: var(--surface);
  color: var(--text);
  border-radius: 6px;
  padding: 3px 8px;
  font-size: 12px;
  font-family: inherit;
}
#sort-key { flex: 1; min-width: 0; }
#sort-direction { cursor: pointer; min-width: 86px; }
#sort-direction:disabled { cursor: default; color: var(--muted); background: var(--hover); }
#sort-key:focus, #sort-direction:focus { border-color: var(--sel-bar); outline: none; }

#search {
  flex: 1;
  min-width: 160px;
  max-width: 280px;
  border: 1.5px solid var(--border);
  border-radius: 6px;
  padding: 3px 10px;
  font-size: 13px;
  outline: none;
  font-family: inherit;
  background: var(--surface);
  color: var(--text);
}
#search:focus { border-color: var(--sel-bar); }
#count {
  font-size: 11px;
  color: var(--muted);
  white-space: nowrap;
}

/* ── Main split ─────────────────────────────── */
#main { display: flex; flex: 1; overflow: hidden; }

/* ── List panel ─────────────────────────────── */
#list-panel {
  width: var(--list-w);
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  border-right: 1px solid var(--border);
  background: var(--surface);
}
#list-toolbar {
  flex-shrink: 0;
  padding: 8px 10px;
  border-bottom: 1px solid var(--border);
  background: var(--surface);
}
.list-toolbar-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 5px;
}
#list-toolbar .flabel { min-width: auto; }
#list { flex: 1; overflow-y: auto; }

.list-row {
  padding: 9px 12px 8px;
  border-bottom: 1px solid var(--border);
  cursor: pointer;
  border-left: 3px solid transparent;
  transition: background .08s;
}
.list-row:hover { background: var(--hover); }
.list-row.selected { background: var(--sel-bg); border-left-color: var(--sel-bar); }

.row-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 3px;
}
.row-dots { display: flex; gap: 4px; align-items: center; }
.dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
  display: inline-block;
}
.row-type {
  font-size: 9px;
  color: #fff;
  padding: 1px 6px;
  border-radius: 3px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .04em;
  flex-shrink: 0;
}
.row-review {
  font-size: 9px; color: #92400e; background: #fef3c7;
  border: 1px solid #f59e0b; padding: 0 5px; border-radius: 3px;
  font-weight: 700; text-transform: uppercase; letter-spacing: .04em;
}
.row-title {
  font-size: 12.5px;
  font-weight: 500;
  line-height: 1.35;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  margin-bottom: 5px;
}
.row-meta { display: flex; align-items: center; gap: 6px; }
.row-year { font-size: 11px; color: var(--muted); min-width: 28px; flex-shrink: 0; }
.depth-bar-wrap {
  flex: 1;
  height: 3px;
  background: var(--border);
  border-radius: 2px;
  overflow: hidden;
}
.depth-bar { height: 100%; border-radius: 2px; }
.depth-label { font-size: 10px; color: var(--muted); min-width: 72px; text-align: right; flex-shrink: 0; }

/* ── Detail panel ───────────────────────────── */
#detail-panel { flex: 1; overflow-y: auto; background: var(--bg); }
#detail-empty {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: var(--muted);
  font-size: 13px;
}
#detail { max-width: 820px; padding: 20px 24px 48px; }

.detail-badges { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 10px; }
.pillar-badge {
  color: #fff; padding: 2px 10px; border-radius: 999px;
  font-size: 11px; font-weight: 600;
}
.type-badge {
  color: #fff; padding: 2px 9px; border-radius: 4px;
  font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: .04em;
}
.depth-badge {
  padding: 1px 9px; border-radius: 999px;
  font-size: 11px; border: 1.5px solid; background: #fff;
}
.review-badge {
  padding: 1px 9px; border-radius: 999px; font-size: 11px;
  border: 1.5px solid #f59e0b; color: #92400e; background: #fef3c7;
  font-weight: 700;
}

.detail-title { font-size: 17px; font-weight: 700; line-height: 1.35; margin-bottom: 6px; }
.detail-authors { font-size: 12.5px; color: var(--muted); margin-bottom: 4px; }
.detail-venue {
  display: flex; flex-wrap: wrap; align-items: center;
  gap: 6px; font-size: 12.5px; margin-bottom: 2px;
}
.detail-year { font-weight: 600; }
.detail-journal { color: var(--muted); }
a.doi-link { color: #2563eb; font-size: 12px; text-decoration: none; }
a.doi-link:hover { text-decoration: underline; }

.dsec {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 14px 16px;
  margin-top: 10px;
}
.dsec h3 {
  font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .08em; color: var(--muted); margin-bottom: 9px;
}
.abstract-p { font-size: 13px; line-height: 1.65; }

.flist {
  font-size: 13px; line-height: 1.5;
  padding-left: 16px;
  display: flex; flex-direction: column; gap: 5px;
}

.tags-row { display: flex; flex-wrap: wrap; gap: 5px; }
.tag { padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 500; }
.t-method { background: #dbeafe; color: #1e40af; }
.t-tool   { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; }
.t-topic  { background: #f3f4f6; color: #374151; }
.t-evid   { background: #fef3c7; color: #92400e; }

.claim-item {
  padding: 9px 11px;
  background: #fffbeb;
  border-left: 3px solid #d97706;
  border-radius: 0 5px 5px 0;
  margin-bottom: 7px;
}
.claim-text { font-size: 13px; line-height: 1.5; font-style: italic; margin-bottom: 5px; }
.claim-meta { display: flex; align-items: center; gap: 6px; }
.claim-loc { font-size: 11px; color: var(--muted); }

.num-tbl { width: 100%; border-collapse: collapse; font-size: 12px; }
.num-tbl th {
  text-align: left; font-weight: 600; color: var(--muted);
  padding: 4px 8px; border-bottom: 1px solid var(--border); font-size: 11px;
}
.num-tbl td { padding: 6px 8px; border-bottom: 1px solid var(--border); vertical-align: top; }
.num-tbl tr:last-child td { border-bottom: none; }
.num-tbl tr.pri td { background: #f0fdf4; }
.num-val { font-weight: 700; white-space: nowrap; }
.num-unit { font-weight: 400; color: var(--muted); font-size: 10px; }
.num-comp { color: var(--muted); font-size: 11px; }
.num-locc { color: var(--muted); font-size: 11px; }
.num-desc { max-width: 220px; }

.prov-grid {
  display: grid; grid-template-columns: auto 1fr; gap: 4px 14px; font-size: 13px;
}
.prov-k {
  font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .05em; color: var(--muted); padding-top: 2px;
}
.prov-v { color: var(--text); line-height: 1.45; }
.prov-notes { font-size: 12px; color: var(--muted); }

.rel-group { display: flex; flex-wrap: wrap; align-items: baseline; gap: 5px; margin-bottom: 5px; }
.rel-lbl {
  font-size: 10px; font-weight: 700; text-transform: uppercase;
  color: var(--muted); letter-spacing: .05em;
}
.rel-link {
  color: #2563eb; cursor: pointer; font-size: 11.5px;
  padding: 2px 8px; background: #eff6ff; border-radius: 4px;
  transition: background .1s;
}
.rel-link:hover { background: #dbeafe; }
</style>
</head>
<body>

<div id="filters">
  <div class="frow">
    <span class="flabel">Pillars</span>
    <button class="chip" data-pillar="hybrid_foundations">Hybrid / Neural ODE</button>
    <button class="chip" data-pillar="uq_identifiability">UQ &amp; Identifiability</button>
    <button class="chip" data-pillar="optimal_control_rl">RL / Optimal Control</button>
    <button class="chip" data-pillar="generative_ai">Generative AI / LLM</button>
  </div>
  <div class="frow">
    <span class="flabel">Type</span>
    <button class="chip" data-type="paper">paper</button>
    <button class="chip" data-type="preprint">preprint</button>
    <button class="chip" data-type="background">background</button>
    <button class="chip" data-type="web">web</button>
    <button class="chip" data-type="report">report</button>
    <button class="chip" data-type="working_doc">working doc</button>
    <span class="fsep"></span>
    <span class="flabel">Depth</span>
    <button class="chip" data-depth="full_text">full text</button>
    <button class="chip" data-depth="sections_key">key sections</button>
    <button class="chip" data-depth="abstract_only">abstract</button>
    <span class="fsep"></span>
    <span class="flabel">Review</span>
    <button class="chip" data-review="draft">draft</button>
    <button class="chip" data-review="reviewed">reviewed</button>
    <input id="search" type="search" placeholder="Search title, author, topic…">
  </div>
</div>

<div id="main">
  <div id="list-panel">
    <div id="list-toolbar">
      <div class="list-toolbar-head">
        <span class="flabel">Papers</span>
        <span id="count" aria-live="polite"></span>
      </div>
      <div class="sort-group">
        <label class="flabel" for="sort-key">Sort</label>
        <select id="sort-key" title="Choose how the visible sources are ordered">
          <option value="default">Library order (default)</option>
          <option value="author">First author</option>
          <option value="year">Year</option>
          <option value="title">Title</option>
          <option value="source_type">Source type</option>
          <option value="relevance">Relevance</option>
          <option value="read_depth">Read depth</option>
          <option value="review_status">Review status</option>
        </select>
        <button id="sort-direction" type="button" disabled title="The default preserves the curated source-index order">Index order</button>
      </div>
    </div>
    <div id="list"></div>
  </div>
  <div id="detail-panel">
    <div id="detail-empty">&#8592; select a source to read</div>
    <div id="detail" style="display:none"></div>
  </div>
</div>

<script>
const SOURCES = __SOURCES_JSON__;

const PILLAR = {
  hybrid_foundations: { label: "Hybrid / Neural ODE",  color: "#2563eb" },
  uq_identifiability: { label: "UQ & Identifiability", color: "#d97706" },
  optimal_control_rl: { label: "RL / Optimal Control", color: "#16a34a" },
  generative_ai:      { label: "Generative AI / LLM",  color: "#7c3aed" }
};
const TYPE = {
  paper:       { label: "paper",       color: "#374151" },
  preprint:    { label: "preprint",    color: "#b45309" },
  background:  { label: "background",  color: "#0d9488" },
  web:         { label: "web",         color: "#0284c7" },
  report:      { label: "report",      color: "#4338ca" },
  working_doc: { label: "working doc", color: "#dc2626" }
};
const DEPTH = {
  full_text:    { label: "full text",    width: "100%", color: "#16a34a" },
  sections_key: { label: "key sections", width: "55%",  color: "#d97706" },
  abstract_only:{ label: "abstract",     width: "25%",  color: "#9ca3af" }
};

const state = {
  selected: null,
  pillars: [],
  types: [],
  depths: [],
  reviews: [],
  q: "",
  sortKey: "default",
  sortDirection: "asc"
};
const SOURCE_ORDER = new Map(SOURCES.map(function(source, index) { return [source.id, index]; }));
const TEXT_COLLATOR = new Intl.Collator(undefined, { numeric: true, sensitivity: "base" });
const RELEVANCE_ORDER = { high: 0, medium: 1, low: 2 };
const DEPTH_ORDER = { full_text: 0, sections_key: 1, abstract_only: 2 };
const REVIEW_ORDER = { draft: 0, reviewed: 1, legacy: 2 };

// ── Helpers ─────────────────────────────────────────────
function esc(s) {
  if (s == null) return "";
  return String(s)
    .replace(/&/g,"&amp;").replace(/</g,"&lt;")
    .replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}
function toggle(arr, v) {
  const i = arr.indexOf(v);
  if (i >= 0) arr.splice(i,1); else arr.push(v);
}
function byId(id) { return document.getElementById(id); }

function sourceTitle(source) {
  return source.title_short || source.title || source.id;
}
function primaryAuthor(source) {
  const author = source.authors && source.authors.length ? String(source.authors[0]).trim() : "";
  return author.includes(",") ? author.split(",", 1)[0].trim() : author;
}
function sortValue(source, key) {
  if (key === "author") return primaryAuthor(source);
  if (key === "year") return source.year;
  if (key === "title") return sourceTitle(source);
  if (key === "source_type") return source.source_type;
  if (key === "relevance") return RELEVANCE_ORDER[source.relevance && source.relevance.relevance_score];
  if (key === "read_depth") return DEPTH_ORDER[source.provenance && source.provenance.read_depth];
  if (key === "review_status") return REVIEW_ORDER[source.review_status || "legacy"];
  return SOURCE_ORDER.get(source.id);
}
function missingSortValue(value) {
  return value == null || value === "";
}
function compareSortValues(left, right) {
  if (typeof left === "number" && typeof right === "number") return left - right;
  return TEXT_COLLATOR.compare(String(left), String(right));
}
function sortedSources(sources) {
  return sources.slice().sort(function(leftSource, rightSource) {
    const left = sortValue(leftSource, state.sortKey);
    const right = sortValue(rightSource, state.sortKey);
    const leftMissing = missingSortValue(left);
    const rightMissing = missingSortValue(right);
    if (leftMissing !== rightMissing) return leftMissing ? 1 : -1;

    var comparison = leftMissing ? 0 : compareSortValues(left, right);
    if (comparison && state.sortDirection === "desc") comparison = -comparison;
    if (comparison) return comparison;

    const titleComparison = TEXT_COLLATOR.compare(sourceTitle(leftSource), sourceTitle(rightSource));
    if (titleComparison) return titleComparison;
    return SOURCE_ORDER.get(leftSource.id) - SOURCE_ORDER.get(rightSource.id);
  });
}
function updateSortDirectionControl() {
  const button = byId("sort-direction");
  if (state.sortKey === "default") {
    button.disabled = true;
    button.textContent = "Index order";
    button.title = "The default preserves the curated source-index order";
    button.setAttribute("aria-label", "Curated source-index order");
    return;
  }

  button.disabled = false;
  const labels = {
    author: { asc: "A to Z", desc: "Z to A" },
    year: { asc: "Oldest first", desc: "Newest first" },
    title: { asc: "A to Z", desc: "Z to A" },
    source_type: { asc: "A to Z", desc: "Z to A" },
    relevance: { asc: "High to low", desc: "Low to high" },
    read_depth: { asc: "Full to abstract", desc: "Abstract to full" },
    review_status: { asc: "Draft to legacy", desc: "Legacy to draft" }
  };
  button.textContent = labels[state.sortKey][state.sortDirection];
  button.title = "Reverse the current sort direction";
  button.setAttribute("aria-label", "Reverse sort direction; currently " + button.textContent);
}

// ── Filter ──────────────────────────────────────────────
function filtered() {
  return SOURCES.filter(s => {
    const pillars = s.relevance && s.relevance.pillars ? s.relevance.pillars : [];
    if (state.pillars.length && !state.pillars.some(p => pillars.includes(p))) return false;
    if (state.types.length  && !state.types.includes(s.source_type)) return false;
    const depth = s.provenance ? s.provenance.read_depth : null;
    if (state.depths.length && !state.depths.includes(depth)) return false;
    if (state.reviews.length && !state.reviews.includes(s.review_status || "legacy")) return false;
    if (state.q) {
      const hay = [
        s.title_short, s.title,
        (s.authors || []).join(" "),
        (s.relevance && s.relevance.topics ? s.relevance.topics : []).join(" "),
        (s.content && s.content.abstract_summary ? s.content.abstract_summary : "")
      ].join(" ").toLowerCase();
      if (!hay.includes(state.q)) return false;
    }
    return true;
  });
}

// ── List ────────────────────────────────────────────────
function renderList() {
  const srcs = sortedSources(filtered());
  byId("count").textContent = srcs.length + " / " + SOURCES.length;
  const list = byId("list");
  list.innerHTML = "";
  srcs.forEach(function(s) {
    const pillars = s.relevance && s.relevance.pillars ? s.relevance.pillars : [];
    const dk = (s.provenance && s.provenance.read_depth) || "abstract_only";
    const d  = DEPTH[dk] || DEPTH.abstract_only;
    const t  = TYPE[s.source_type] || { label: s.source_type, color: "#888" };
    const row = document.createElement("div");
    row.className = "list-row" + (s.id === state.selected ? " selected" : "");
    row.dataset.id = s.id;
    row.innerHTML =
      "<div class='row-top'>" +
        "<div class='row-dots'>" +
          pillars.map(function(p) {
            var pi = PILLAR[p] || { color:"#ccc", label:p };
            return "<span class='dot' style='background:" + pi.color + "' title='" + esc(pi.label) + "'></span>";
          }).join("") +
        "</div>" +
        (s.review_status === "draft" ? "<span class='row-review'>draft</span>" : "") +
        "<span class='row-type' style='background:" + t.color + "'>" + t.label + "</span>" +
      "</div>" +
      "<div class='row-title'>" + esc(s.title_short || s.title || s.id) + "</div>" +
      "<div class='row-meta'>" +
        "<span class='row-year'>" + (s.year || "—") + "</span>" +
        "<div class='depth-bar-wrap' title='" + d.label + "'>" +
          "<div class='depth-bar' style='width:" + d.width + ";background:" + d.color + "'></div>" +
        "</div>" +
        "<span class='depth-label'>" + d.label + "</span>" +
      "</div>";
    row.addEventListener("click", function() {
      state.selected = s.id;
      renderList();
      renderDetail(s);
    });
    list.appendChild(row);
  });
}

// ── Detail ──────────────────────────────────────────────
function renderDetail(s) {
  byId("detail-empty").style.display = "none";
  const el = byId("detail");
  el.style.display = "block";

  const pillars = s.relevance && s.relevance.pillars ? s.relevance.pillars : [];
  const dk  = (s.provenance && s.provenance.read_depth) || "abstract_only";
  const d   = DEPTH[dk] || DEPTH.abstract_only;
  const t   = TYPE[s.source_type] || { label: s.source_type, color: "#888" };
  const c   = s.content   || {};
  const rel = s.relevance  || {};
  const prov= s.provenance || {};
  const rels= s.relationships || {};

  var doiHtml = "";
  if (s.doi) {
    doiHtml = "<a class='doi-link' href='https://doi.org/" + esc(s.doi) + "' target='_blank' rel='noopener'>doi:" + esc(s.doi) + "</a>";
  } else if (s.url) {
    doiHtml = "<a class='doi-link' href='" + esc(s.url) + "' target='_blank' rel='noopener'>" + esc(s.url) + "</a>";
  }

  var kfHtml     = (c.key_findings     || []).map(function(f) { return "<li>" + esc(f) + "</li>"; }).join("");
  var methHtml   = (c.methods_discussed|| []).map(function(m) { return "<span class='tag t-method'>" + esc(m.replace(/_/g," ")) + "</span>"; }).join("");
  var toolHtml   = (c.tools_software   || []).map(function(m) { return "<span class='tag t-tool'>"   + esc(m)                  + "</span>"; }).join("");
  var topHtml    = (rel.topics         || []).map(function(m) { return "<span class='tag t-topic'>"  + esc(m.replace(/_/g," ")) + "</span>"; }).join("");
  var gapsHtml   = (rel.gaps_addressed || []).map(function(g) { return "<li>" + esc(g) + "</li>"; }).join("");

  var claimsHtml = (c.extracted_claims || []).map(function(cl) {
    return "<div class='claim-item'>" +
      "<div class='claim-text'>" + esc(cl.text) + "</div>" +
      "<div class='claim-meta'><span class='tag t-evid'>" + esc(cl.evidence_type) + "</span>" +
        "<span class='claim-loc'>" + esc(cl.location) + "</span></div>" +
      "</div>";
  }).join("");

  var nums = c.numerical_findings || [];
  var numHtml = "";
  if (nums.length) {
    numHtml = "<div class='dsec'><h3>Numerical Findings</h3>" +
      "<table class='num-tbl'><thead><tr><th>Metric</th><th>Value</th><th>vs.</th><th>Location</th></tr></thead><tbody>" +
      nums.map(function(n) {
        return "<tr class='" + (n.is_primary_finding ? "pri" : "") + "'>" +
          "<td class='num-desc'>" + esc(n.description) + "</td>" +
          "<td><span class='num-val'>" + esc(n.value) + "</span>" +
            (n.unit ? " <span class='num-unit'>" + esc(n.unit) + "</span>" : "") + "</td>" +
          "<td class='num-comp'>" + (n.comparison_baseline ? esc(n.comparison_baseline) : "—") + "</td>" +
          "<td class='num-locc'>" + esc(n.location) + "</td>" +
          "</tr>";
      }).join("") +
      "</tbody></table></div>";
  }

  function relGroup(ids, label) {
    if (!ids || !ids.length) return "";
    var links = ids.map(function(id) {
      var found = SOURCES.find(function(x) { return x.id === id; });
      var name  = found ? (found.title_short || found.title || id) : id;
      return "<span class='rel-link' data-id='" + esc(id) + "'>" + esc(name) + "</span>";
    }).join("");
    return "<div class='rel-group'><span class='rel-lbl'>" + label + "</span>" + links + "</div>";
  }
  var relHtml = [
    relGroup(rels.cites,       "Cites"),
    relGroup(rels.cited_by,    "Cited by"),
    relGroup(rels.extends,     "Extends"),
    relGroup(rels.contradicts, "Contradicts"),
  ].filter(Boolean).join("");

  var auth = (s.authors || []).join(", ");

  el.innerHTML =
    "<div class='detail-badges'>" +
      pillars.map(function(p) {
        var pi = PILLAR[p] || { color:"#888", label:p };
        return "<span class='pillar-badge' style='background:" + pi.color + "'>" + esc(pi.label) + "</span>";
      }).join("") +
      "<span class='type-badge' style='background:" + t.color + "'>" + t.label + "</span>" +
      "<span class='depth-badge' style='border-color:" + d.color + ";color:" + d.color + "'>" + d.label + "</span>" +
      (s.review_status === "draft" ? "<span class='review-badge'>Draft - human review required</span>" : "") +
      (s.review_status === "reviewed" ? "<span class='review-badge' style='border-color:#16a34a;color:#166534;background:#dcfce7'>Human reviewed</span>" : "") +
    "</div>" +
    "<h1 class='detail-title'>" + esc(s.title || s.title_short || s.id) + "</h1>" +
    (auth ? "<div class='detail-authors'>" + esc(auth) + "</div>" : "") +
    "<div class='detail-venue'>" +
      (s.year           ? "<span class='detail-year'>"    + s.year                    + "</span>" : "") +
      (s.journal_or_venue ? "<span class='detail-journal'>" + esc(s.journal_or_venue) + "</span>" : "") +
      doiHtml +
    "</div>" +

    "<div class='dsec'><h3>Abstract Summary</h3>" +
      "<p class='abstract-p'>" + esc(c.abstract_summary || "—") + "</p></div>" +

    (kfHtml   ? "<div class='dsec'><h3>Key Findings</h3><ul class='flist'>" + kfHtml + "</ul></div>" : "") +

    (methHtml || toolHtml
      ? "<div class='dsec'><h3>Methods &amp; Tools</h3><div class='tags-row'>" + methHtml + toolHtml + "</div></div>"
      : "") +

    (claimsHtml ? "<div class='dsec'><h3>Extracted Claims</h3>" + claimsHtml + "</div>" : "") +

    numHtml +

    (gapsHtml ? "<div class='dsec'><h3>Gaps Addressed</h3><ul class='flist'>" + gapsHtml + "</ul></div>" : "") +

    (topHtml  ? "<div class='dsec'><h3>Topics</h3><div class='tags-row'>" + topHtml + "</div></div>" : "") +

    "<div class='dsec'><h3>Provenance</h3><div class='prov-grid'>" +
      "<span class='prov-k'>Read depth</span><span class='prov-v' style='color:" + d.color + "'>" + d.label + "</span>" +
      "<span class='prov-k'>Date read</span><span class='prov-v'>"    + esc(prov.date_read    || "—") + "</span>" +
      "<span class='prov-k'>How obtained</span><span class='prov-v'>" + esc(prov.how_obtained || "—") + "</span>" +
      "<span class='prov-k'>Read by</span><span class='prov-v'>"      + esc(prov.read_by      || "—") + "</span>" +
      "<span class='prov-k'>Review status</span><span class='prov-v'>" + esc(s.review_status || "legacy / not recorded") + "</span>" +
      (s.reviewed_by ? "<span class='prov-k'>Reviewed by</span><span class='prov-v'>" + esc(s.reviewed_by) + "</span>" : "") +
      (s.reviewed_date ? "<span class='prov-k'>Review date</span><span class='prov-v'>" + esc(s.reviewed_date) + "</span>" : "") +
      (s.review_notes ? "<span class='prov-k'>Review notes</span><span class='prov-v prov-notes'>" + esc(s.review_notes) + "</span>" : "") +
      (prov.notes ? "<span class='prov-k'>Notes</span><span class='prov-v prov-notes'>" + esc(prov.notes) + "</span>" : "") +
    "</div></div>" +

    (relHtml ? "<div class='dsec'><h3>Related Sources</h3>" + relHtml + "</div>" : "");

  el.querySelectorAll(".rel-link").forEach(function(link) {
    link.addEventListener("click", function() {
      var id  = link.dataset.id;
      var src = SOURCES.find(function(x) { return x.id === id; });
      if (!src) return;
      state.selected = id;
      renderList();
      renderDetail(src);
      var row = document.querySelector(".list-row[data-id='" + id + "']");
      if (row) row.scrollIntoView({ block: "nearest" });
    });
  });

  el.parentElement.scrollTop = 0;
}

// ── Chip wiring ──────────────────────────────────────────
document.querySelectorAll("[data-pillar]").forEach(function(btn) {
  btn.addEventListener("click", function() {
    var p = btn.dataset.pillar;
    toggle(state.pillars, p);
    document.querySelectorAll("[data-pillar]").forEach(function(b) {
      var active = state.pillars.includes(b.dataset.pillar);
      var color  = (PILLAR[b.dataset.pillar] || {color:"#888"}).color;
      b.style.background   = active ? color : "";
      b.style.borderColor  = active ? color : "";
      b.style.color        = active ? "#fff" : "";
    });
    renderList();
  });
});

document.querySelectorAll("[data-type]").forEach(function(btn) {
  btn.addEventListener("click", function() {
    toggle(state.types, btn.dataset.type);
    btn.classList.toggle("active", state.types.includes(btn.dataset.type));
    renderList();
  });
});

document.querySelectorAll("[data-depth]").forEach(function(btn) {
  btn.addEventListener("click", function() {
    toggle(state.depths, btn.dataset.depth);
    btn.classList.toggle("active", state.depths.includes(btn.dataset.depth));
    renderList();
  });
});

document.querySelectorAll("[data-review]").forEach(function(btn) {
  btn.addEventListener("click", function() {
    toggle(state.reviews, btn.dataset.review);
    btn.classList.toggle("active", state.reviews.includes(btn.dataset.review));
    renderList();
  });
});

document.getElementById("search").addEventListener("input", function(e) {
  state.q = e.target.value.trim().toLowerCase();
  renderList();
});

document.getElementById("sort-key").addEventListener("change", function(e) {
  state.sortKey = e.target.value;
  state.sortDirection = state.sortKey === "year" ? "desc" : "asc";
  updateSortDirectionControl();
  renderList();
});

document.getElementById("sort-direction").addEventListener("click", function() {
  state.sortDirection = state.sortDirection === "asc" ? "desc" : "asc";
  updateSortDirectionControl();
  renderList();
});

updateSortDirectionControl();
renderList();
</script>
</body>
</html>"""


if __name__ == "__main__":
    main()
