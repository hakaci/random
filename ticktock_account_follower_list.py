from TikTokApi import TikTokApi
import asyncio


async def fetch_following(username):
    async with TikTokApi() as api:
        ms_token = '-'  # Replace with your actual ms_token
        
        try:
            # Create TikTokApi session
            await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
            
            # Get User object for given username
            target_user = await api.user(username=username).info()
            
            # Get users that target account is following
            following_list = target_user['following']

            # Sort following list by follower count (descending order)
            sorted_following = sorted(following_list, key=lambda x: x['followerCount'], reverse=True)
            
            # Print or return sorted following list
            for user in sorted_following:
                print(f"Username: {user['uniqueId']}, Follower Count: {user['followerCount']}")
            return sorted_following
        
        except Exception as e:
            print(f"Error fetching following list: {e}")


async def main(username):
    await fetch_following(username)


if __name__ == "__main__":
    username = input("Enter TikTok username: ")
    asyncio.run(main(username))
