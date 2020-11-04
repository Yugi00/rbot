import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment functions from the week_07 lab here

def generate_comment_0():
    
    like_list = ['like', 'really enjoy', 'love', 'appreciate']
    like_item = random.choice(like_list)
    broke_list = ['less fortunate', 'poor', 'broke', 'impoverished']
    broke_item = random.choice(broke_list)
    student_list = ['students', 'kids', 'young people', ' high schoolers']
    student_item = random.choice(student_list)
    college_list = ['school', 'college', 'university', 'an institute']
    college_item = random.choice(college_list)
    minority_list = ['minority', 'less fortunate', 'low economic class', 'poor']
    minority_item = random.choice(minority_list)
    text = 'I ' + like_item + ' how Joe Biden wants to allow ' + broke_item + ' ' + student_item + ' to attend ' + college_item + ' for free. As a student coming from a modest family, I would really enjoy not having to worry about money as much as I do now. Also, students who are part of the ' + minority_item + ' would be given more of an opportunity to attend a university.'
    return text 

def generate_comment_1():
    like_list = ['like', 'really enjoy', 'love', 'appreciate']
    like_item = random.choice(like_list)
    character_list = ['seems like', 'is', 'might be', 'is probably']
    character_item = random.choice(character_list)
    smart_list = ['knowledgable', 'smart', 'interesting', 'intelligent']
    smart_item = random.choice(smart_list)
    calm_list = ['calm', 'composed', 'relaxed', 'unflustered']
    calm_item = random.choice(calm_list)
    trump_list = ['trump', 'the orange', 'Mr. Build-a-wall', 'Mr. MAGA']
    trump_item = random.choice(trump_list)
    text = 'I ' + like_item + ' how Pamela Harris is the running partner for Joe Biden. She ' + character_item + ' a very ' + smart_item + ' and ' + calm_item + ' politician compared to ' + trump_item + ' and his running partner. '
    return text 

def generate_comment_2():
    think_list = ['think', 'believe', 'suspect', 'trust']
    think_item = random.choice(think_list)
    health_list = ['healthare', 'medical care', 'health insurance', 'medical insurance']
    health_item = random.choice(health_list)
    good_list = ['really good', 'great', 'amazing', 'fantastic']
    good_item = random.choice(good_list)
    country_list = ['country', 'state', 'USA', 'nation']
    country_item = random.choice(country_list)
    afford_list = ['afford', 'pay for', 'buy', 'own']
    afford_item = random.choice(afford_list)
    text = 'I ' + think_item + ' that the plan Biden has for ' + health_item + ' is ' + good_item + ' for the ' + country_item + '. Many people are unable to ' + afford_item + ' healthcare on their own and because of this are unable to receive any treatment they need to be the healthiest they can be.'
    return text 

def generate_comment_3():
    think_list = ['think', 'believe', 'suspect', 'suppose']
    think_item = random.choice(think_list)
    trump_list = ['trump', 'the orange', 'Mr. Build-a-wall', 'Mr. MAGA']
    trump_item = random.choice(trump_list)
    bad_list = ['bad', 'poor', 'terrible', 'disgraceful']
    bad_item = random.choice(bad_list)
    attitude_list = ['His attitude', 'His mindset', 'His beliefs', 'His way of thinking']
    attitude_item = random.choice(attitude_list)
    sad_list = ['sad', 'embarrassed', 'uncomfortable', 'ashamed']
    sad_item = random.choice(sad_list)
    text = 'So far I ' + think_item + ' that ' + trump_item + ' has done a ' + bad_item + ' job when it comes to being President. ' + attitude_item +  ' and the way he acts honestly makes me ' + sad_item + ' to call myself an American.'
    return text 

def generate_comment_4():
    trump_list = ['trump', 'the orange', 'Mr. Build-a-wall', 'Mr. MAGA']
    trump_item = random.choice(trump_list)
    think_list = ['think', 'believe', 'suspect', 'trust']
    think_item = random.choice(think_list)
    voted_list = ['be re-elected', 'be put back into office', 'receive another term', 'be voted for']
    voted_item = random.choice(voted_list)
    angry_list = ['angry', 'upset', 'disappointed', 'mad']
    angry_item = random.choice(angry_list)
    country_list = ['this country', 'the USA', 'this nation', 'this state']
    country_item = random.choice(country_list)
    text = 'I do not ' + think_item + ' that ' + trump_item + ' should ' + voted_item + ' because he is a complete rascist. Even during his first presidential race he made it clear that he did not like having immigrants in the country. Coming from a family who immigrated to the US, this makes me very uneasy and ' + angry_item + ' as it makes me feel as though my family and I are not accepted in ' + country_item + '.'
    return text 

def generate_comment_5():
    trump_list = ['Trump', 'the orange', 'Mr. Build-a-wall', 'Mr. MAGA']
    trump_item = random.choice(trump_list)
    smart_list = ['knowledgable', 'smart', 'a genius', 'intelligent']
    smart_item = random.choice(smart_list)
    business_list = ['a businessman', 'an entrepreneur', 'a tycoon', 'a speculator']
    business_item = random.choice(business_list)
    politics_list = ['politics', 'government', 'government policies', 'state affairs']
    politics_item = random.choice(politics_list)
    bankrupt_list = ['bankrupt', 'terribly', 'down the drain', 'comletely flat']
    bankrupt_item = random.choice(bankrupt_list)
    text = trump_item + ' is not ' + smart_item + ' when it comes to ' + politics_item + '. He is more of ' + business_item + ' more than anything else, but even then so many of his own businesses have gone ' + bankrupt_item + '.'
    return text 

def generate_comment():
    comment_list = [generate_comment_0(), generate_comment_1(), generate_comment_2(), generate_comment_3(), generate_comment_4(), generate_comment_5()]
    comment_item = random.choice(comment_list)
    text = comment_item
    return text




# connect to reddit 
reddit = praw.Reddit('reddit-bot')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jiwfn3/from_hoangs_bot_1_biden_pledges_ambitious_climate/'
submission = reddit.submission(url=reddit_debate_url)
subreddit = reddit.subreddit('csci040temp')

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []

    submission.comments.replace_more(limit=10)
    for comment in submission.comments.list():
        all_comments.append(comment)
    #print('all_comments = ', all_comments)
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    
    not_my_comments = []
    for comment in all_comments:
        if comment.author != 'DarthBot27':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    

    if has_not_commented == True:
        
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
        
        submission.reply(generate_comment())
            
    else:
        comments_without_replies = []
        for comment in not_my_comments:
            for reply in comment.replies:
                if reply.author != 'DarthBot27':
                    comments_without_replies.append(comment)
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
        try:
            comment_reply = random.choice(comments_without_replies)
            my_reply = reddit.comment(id = comment_reply)
            my_reply.reply(generate_comment())
        except IndexError:
            len(comments_without_replies) == 0
            print('index error')
        
        except praw.exceptions.APIException:
            print('exception found')
            time.sleep(60)
            print('done sleeping')

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions
    random_thread = random.random()
    if random_thread < .5:
        submission = reddit.submission(url= reddit_debate_url)
    else:
        top_threads = list(reddit.subreddit('csci040temp').top(time_filter='all'))
        top_threads.append(submission)
        random_submission = random.choice(top_threads)
        print('random_submission = ', random_submission)
        submission = reddit.submission(id = random_submission)
    """
    #Extra credit
    #Upvote submissions
    canidates = ['joe', 'biden', 'kamala', 'harris', 'joe biden', 'kamala harris']
    sub_title = submission.title.lower()
    for candidate in canidates:
        if candidate in sub_title:
            submission.upvote()

    #Upvote comments
    canidates = ['joe', 'biden', 'kamala', 'harris', 'joe biden', 'kamala harris']
    for comment in submission.comments.list():
        for candidate in canidates:
            if candidate in comment.body:
                comment.upvote()
    """    
