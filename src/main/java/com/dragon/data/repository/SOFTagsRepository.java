package com.dragon.data.repository;

import com.dragon.data.domain.SOFTags;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

@Repository
public interface SOFTagsRepository extends JpaRepository<SOFTags,Integer> {

    @Query(value = "SELECT SUM(s.tag_points) FROM hackathon.stackoverflow_tags s", nativeQuery = true)
    long countAllSkill();
}
