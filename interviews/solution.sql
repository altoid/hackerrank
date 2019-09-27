use hackerrank_interviews;

select
contests.*,
agg.tot_submits,
agg.tot_acc_submits,
agg.tot_views,
agg.tot_unique_views
from contests
inner join
(
    select
    contest_id,
    sum(tot_submits) tot_submits,
    sum(tot_acc_submits) tot_acc_submits, 
    sum(tot_views) tot_views,
    sum(tot_unique_views)  tot_unique_views
    from
    (
        select
        contests.contest_id,
        ifnull(condensed_submission_stats.total_submissions, 0) tot_submits,
        ifnull(condensed_submission_stats.total_accepted_submissions, 0) tot_acc_submits,
        ifnull(condensed_view_stats.total_views, 0) tot_views,
        ifnull(condensed_view_stats.total_unique_views, 0) tot_unique_views
        from contests
        inner join colleges on contests.contest_id = colleges.contest_id
        inner join challenges on challenges.college_id = colleges.college_id
        left join
        (
            select
            challenge_id, sum(total_submissions) total_submissions, sum(total_accepted_submissions) total_accepted_submissions
            from
            submission_stats
            group by challenge_id
        ) condensed_submission_stats
        on condensed_submission_stats.challenge_id = challenges.challenge_id
        left join
        (
            select
            challenge_id, sum(total_views) total_views, sum(total_unique_views) total_unique_views
            from
            view_stats
            group by challenge_id
        ) condensed_view_stats
        on condensed_view_stats.challenge_id = challenges.challenge_id
    ) intermediate
    group by contest_id
    having
    sum(tot_submits)  +
    sum(tot_acc_submits) +
    sum(tot_views) +
    sum(tot_unique_views) > 0
) agg on agg.contest_id = contests.contest_id
;
