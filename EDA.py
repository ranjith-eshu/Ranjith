p_match_summary_plot4 <- (p_player_of_match / p_matches_seasons) + plot_layout(guides = 'collect') + 
  plot_annotation(title = "IPL Matches", 
                  subtitle = "Critical Stats 2008 - 2019",  
                  theme = theme_solarized_2(light = FALSE, base_size = 12) + theme(plot.title = element_text(color = "white"), 
                                                                                   plot.subtitle = element_text(color = "white")))

ggsave(filename = "match_summary_plot4.png", 
       plot = p_match_summary_plot4)
