
tbl_win_by_wickets <- select(tbl_ipl_data, 
       id, 
       winner, 
       win_by_runs, 
       win_by_wickets) %>% 
  filter(win_by_wickets != 0 & !is.na(win_by_wickets)) %>%
  group_by(win_by_wickets) %>%
  mutate(count = n()) %>% 
  ungroup()

p_win_wickets_freq <- ggplot(data = tbl_win_by_wickets) + 
geom_area(mapping = aes(x = win_by_wickets), 
              stat = "count",
              show.legend = FALSE, 
              color = "red", 
              fill = "turquoise", 
              size = 1) +
geom_vline(xintercept = unique(tbl_win_by_wickets$win_by_wickets[tbl_win_by_wickets$count == max(tbl_win_by_wickets$count)])
, linetype = "dashed", color = "red") + 
scale_x_continuous(breaks = c(0, 2, 4, 6, 8, 10), 
                   labels = c(0, 2, 4, 6, 8, 10)) +  
  theme_solarized_2(light = FALSE, base_size = 14) + 
  theme(axis.text.x = element_text(color = "white"), 
        axis.text.y = element_text(color = "white"),
        axis.title.x = element_text(color = "white"),
        axis.title.y = element_text(color = "white"), 
        plot.title = element_text(color = "white"),
        strip.text = element_text(color = "white"),
        legend.text = element_text(color = "white"), 
        legend.title = element_text(color = "white"), 
        legend.position = "top") +
  labs(x = "Win by Wickets", 
       y = "Wins")
