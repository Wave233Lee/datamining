package com.dragon.data.repository;

import com.dragon.data.domain.UserTags;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

@Repository
public interface UserTagsRepository extends JpaRepository<UserTags,Integer> {

    /**
     * 某专项技能人数统计
     * @param tags
     * @return
     */
    @Query(value = "SELECT COUNT(*) FROM hackathon.score_tags s WHERE s.tags_name = ?1", nativeQuery = true)
    Integer countTags(String tags);
    /**
     * 某技能排行
     * @param tags
     * @param score
     * @return
     */
    @Query(value = "SELECT COUNT(*) FROM hackathon.score_tags s WHERE s.tags_name = ?1 AND s.tags_score > ?2", nativeQuery = true)
    double rankByTags(String tags, Integer score);

    @Query(value = "SELECT * FROM hackathon.user_tags s WHERE s.userid = ?1", nativeQuery = true)
    UserTags findOneByUid(Integer userid);
}
