package com.dragon.data.repository;

import com.dragon.data.domain.ScoreTags;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ScoreTagsRepository extends JpaRepository<ScoreTags,Integer> {
}
