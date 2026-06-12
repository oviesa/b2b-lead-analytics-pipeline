-- Leads per channel with conversion rate
SELECT
    c.name AS channel,
    COUNT(DISTINCT le.lead_id) AS total_leads,
    COUNT(DISTINCT CASE WHEN ls.status = 'converted' THEN ls.lead_id END) AS converted,
    ROUND(
        COUNT(DISTINCT CASE WHEN ls.status = 'converted' THEN ls.lead_id END)::numeric
        / NULLIF(COUNT(DISTINCT le.lead_id), 0) * 100, 2
    ) AS conversion_rate_pct
FROM lead_events le
JOIN channels c ON le.channel_id = c.channel_id
LEFT JOIN lead_status ls ON le.lead_id = ls.lead_id
GROUP BY c.name
ORDER BY total_leads DESC;

-- Top industries by lead volume
SELECT co.industry, COUNT(l.lead_id) AS lead_count
FROM leads l
JOIN companies co ON l.company_id = co.company_id
GROUP BY co.industry
ORDER BY lead_count DESC;

-- Monthly lead trend
SELECT DATE_TRUNC('month', created_at) AS month, COUNT(*) AS new_leads
FROM leads
GROUP BY month
ORDER BY month;