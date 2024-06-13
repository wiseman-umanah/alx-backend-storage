-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
select band_name, sum(split) - sum(formed) as lifespan from metal_bands group by band_name order by lifespan desc;
