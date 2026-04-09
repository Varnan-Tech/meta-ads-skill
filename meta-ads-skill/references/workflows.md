# Meta Ads Workflows

This document outlines complex orchestrations and workflows for common Meta Ads tasks.

## 1. CPA Spike Troubleshooting

When a client or user asks to investigate a spike in Cost Per Action (CPA), follow this systematic approach:

1. **Account Level Overview**
   - **Tool:** `get_ad_accounts` (if account ID not provided)
   - **Tool:** `get_insights` (Level: account)
   - **Action:** Look at overall account performance over the last 7, 14, and 30 days to identify when the spike started.

2. **Campaign Breakdown**
   - **Tool:** `get_campaigns`
   - **Tool:** `get_insights` (Level: campaign)
   - **Action:** Identify which specific campaigns are driving the CPA increase. Compare spend and CPA across active campaigns.

3. **Ad Set Deep Dive**
   - **Tool:** `get_adsets`
   - **Tool:** `get_insights` (Level: adset)
   - **Action:** For the offending campaigns, break down by Ad Set to see if specific audiences or placements are underperforming.

4. **Ad & Creative Analysis**
   - **Tool:** `get_ads`
   - **Tool:** `get_insights` (Level: ad)
   - **Action:** Check if specific ads are experiencing ad fatigue (high frequency, dropping CTR) or if recent changes disrupted the learning phase.

5. **Advanced Insights (Optional)**
   - **Tool:** `analyze_campaigns`
   - **Action:** Run automated analysis on the specific campaigns to generate actionable recommendations.

6. **Synthesis and Reporting**
   - Use the `CPA Spike Investigation Report` template (found in `report_templates.md`) to structure the findings and recommendations.

## 2. New Audience Discovery

When a user wants to find new audiences or test new targeting:

1. **Review Current Top Performers**
   - **Tool:** `get_insights` (Level: adset)
   - **Action:** Identify the ad sets currently delivering the best ROAS/CPA.

2. **Generate Audience Ideas**
   - **Action:** Based on the product and past top performers, generate Lookalike (LAL) audience suggestions or new interest-based targeting.

3. **Structure the Test**
   - Recommend a campaign structure for testing (e.g., A/B testing with Campaign Budget Optimization (CBO) or Ad Set Budget Optimization (ABO)).

4. **Monitoring**
   - Provide the exact metrics to watch (e.g., CTR, CPC, early conversions) over the next 3-7 days.
