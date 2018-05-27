package com.dragon.data.controller;

import com.dragon.data.domain.UserTags;
import com.dragon.data.service.UserTagsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "/userTags")
public class UserTagsController {

    @Autowired
    private  UserTagsService userTagsService;
    /**
     * 查询所有列表
     * @return
     */
    @RequestMapping(value = "/getAll")
    public List<UserTags> userTagsList(){
        return userTagsService.findAll();
    }
    /**
     * 添加一个userTags
     * @return
     *
    @RequestMapping(value = "/add")
    public Result userTagsAdd(@Valid UserTags userTags, BindingResult bindingResult){
        if(bindingResult.hasErrors()){
            return ResultUtil.error(1, bindingResult.getFieldError().getDefaultMessage());
        }
        userTags.set(userTags.getName());
        userTags.setTags(userTags.getTags());
        userTags.setScore(userTags.getScore());
        return ResultUtil.success(userTagsService.save(userTags));
    }
    */
    /**
     * 删除一个userTags
     *
    @RequestMapping(value = "/delete")
    public void userTagsDelete(Integer id){
        userTagsService.delete(id);
    }
*/
    /**
     * 某专项技能人数统计
     * @param tags
     * @return
     */
    @RequestMapping(value = "/count")
    public Integer countTags(String tags){
        return userTagsService.countTags(tags);
    }

    /**
     * 某技能排行
     * @param tags
     * @param score
     * @return
     */
    @RequestMapping(value = "/rank")
    public double rankByTags(String tags, Integer score){
        return (float)(userTagsService.rankByTags(tags, score)+1)/(float)userTagsService.countTags(tags);
    }

    @RequestMapping(value = "/uid")
    public String findOneByUid(Integer userid){
        return userTagsService.findOneByUid(userid);
    }
    /**
     * 根据ID输出技能评分
     * @param userid
     * @return
     */
    @RequestMapping(value = "/point1")
    public double pointByTags1(Integer userid){
        return userTagsService.pointByTags1(userid);
    }

    @RequestMapping(value = "/point2")
    public double pointByTags2(Integer userid){
        return userTagsService.pointByTags2(userid);
    }
    @RequestMapping(value = "/point3")
    public double pointByTags3(Integer userid){
        return userTagsService.pointByTags3(userid);
    }
    @RequestMapping(value = "/point4")
    public double pointByTags4(Integer userid){
        return userTagsService.pointByTags4(userid);
    }
}