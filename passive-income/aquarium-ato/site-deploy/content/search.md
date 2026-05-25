+++
title = "Search"
date = 2026-04-25T20:30:00-04:00
draft = false
description = "Search the live Nano Tank ATO Reliability guide library."
slug = "search"
verification_status = "editorial-live"
affiliate_ready = false
show_disclosure = false
+++

Use the search box below to filter the current live guide library.

<div id="search-app">
  <input id="guide-search" type="search" placeholder="Search guides by topic, problem, or keyword…" style="width:100%;padding:12px 14px;border:1px solid #c7dadd;border-radius:12px;font:inherit;box-sizing:border-box;margin:16px 0 18px;" />
  <div id="search-results"></div>
</div>

<script>
(function () {
  const guides = [
    {
      title: "Why Your ATO Keeps Overfilling a Nano Tank",
      url: "/posts/why-your-ato-keeps-overfilling-a-nano-tank/",
      description: "Troubleshooting overfill behavior, fast triage, and the failure chains that matter most.",
      tags: ["overfill", "salinity", "troubleshooting", "sensor", "siphon"]
    },
    {
      title: "Float Switch vs Optical Sensor ATOs for Nano Tanks",
      url: "/posts/float-switch-vs-optical-sensor-ato-nano-tanks/",
      description: "A reliability-first comparison of the two sensor styles most nano tank owners keep weighing.",
      tags: ["comparison", "float switch", "optical sensor", "sensors", "buying"]
    },
    {
      title: "ATO Maintenance Schedule for Nano Tanks",
      url: "/posts/ato-maintenance-schedule-nano-tanks/",
      description: "A realistic maintenance rhythm for keeping an ATO trustworthy instead of weirdly haunted.",
      tags: ["maintenance", "cleaning", "inspection", "salt creep"]
    },
    {
      title: "How to Stop False ATO Alarms in Small Tanks",
      url: "/posts/how-to-stop-false-ato-alarms-small-tanks/",
      description: "How to troubleshoot nuisance alarms without teaching yourself to ignore the system.",
      tags: ["false alarms", "troubleshooting", "alerts", "maintenance"]
    }
  ];

  const input = document.getElementById('guide-search');
  const results = document.getElementById('search-results');

  function render(items) {
    if (!items.length) {
      results.innerHTML = '<p style="color:#4d6972;">No live guides matched that search yet.</p>';
      return;
    }
    results.innerHTML = items.map(item => `
      <article style="background:#fff;border:1px solid #d9e8ea;border-radius:14px;padding:16px;margin-bottom:12px;box-shadow:0 4px 14px rgba(16,59,74,0.04);">
        <h2 style="margin:0 0 8px;font-size:1.15rem;"><a href="${item.url}">${item.title}</a></h2>
        <p style="margin:0;color:#466671;">${item.description}</p>
      </article>
    `).join('');
  }

  function filter() {
    const q = input.value.trim().toLowerCase();
    if (!q) return render(guides);
    const filtered = guides.filter(item => {
      const haystack = [item.title, item.description, ...(item.tags || [])].join(' ').toLowerCase();
      return haystack.includes(q);
    });
    render(filtered);
  }

  input.addEventListener('input', filter);
  render(guides);
})();
</script>
