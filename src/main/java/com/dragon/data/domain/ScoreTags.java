package com.dragon.data.domain;

import javax.persistence.*;

@Entity
@Table(name = "score_tags")
public class ScoreTags {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;

    @Column(name = "tags_name")
    private String tagsname;

    @Column(name = "tags_score")
    private Integer tagscore;
}
