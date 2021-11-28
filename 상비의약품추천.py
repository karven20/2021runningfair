
while True:
   symptom=input("당신의 증상은 해열,감기,소화불량,화상 중 무엇입니까?")

   if symptom=="해열":
       q2=input("만 12세 이상입니까? (네/아니오):")
   
       if q2=="네":
           print("타이레놀 정 500mg \n1).1일 2~4회 복용. \n2)1일 최대 4캡슐을 초과하여 복용하지 말것.")
           s=input("도움이 더 필요하신가요? (네/아니오):")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break
       elif q2=="아니오":
           print("타이레놀 정 160mg\n1).1일 5회를 초과하여 복용하지 말것.")
           s=input("도움이 더 필요하신가요? (네/아니오):")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break
       else:
           print("해당 증상에 맞는 약을 찾을 수 없습니다.전문가와 상담하세요.")
           s=input("도움이 더 필요하신가요? (네/아니오):")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break
       
   if symptom=="감기":
       q2=input("알약 or 액상 중에 고르시오 : ")
   
       if q2=="알약":
           print("판피린티정\n1).1일 3회 식후 30분에 복용.")
           s=input("도움이 더 필요하신가요? (네/아니오):")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break
       elif q2=="액상":
           print("판콜 A\n1).1일 3회 식후 30분에 복용.")
           s=input("도움이 더 필요하신가요? (네/아니오):")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break
       else:
           print("해당 증상에 맞는 약을 찾을 수 없습니다.전문가와 상담하세요.")
           s=input("도움이 더 필요하신가요? (네/아니오):")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break
       
   if symptom=="소화불량":
       q2=input("만 7세 이하입니까? (네/아니오): ")
   
       if q2=="네":
           print("백초시럽\n1).1회 3회 식후에 복용.")
           s=input("도움이 더 필요하신가요? (네/아니오)")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break
       elif q2=="아니오":
           print("베아제정\n1).1정을 1일 3회 식후에 복용.")
           s=input("도움이 더 필요하신가요? (네/아니오): ")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break
       else:
           print("해당 증상에 맞는 약을 찾을 수 없습니다.전문가와 상담하세요.")
           s=input("도움이 더 필요하신가요? (네/아니오): ")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break
       
   if symptom=="화상":
       q2=input("물집이 생겼나요? (네/아니오): ")
   
       if q2=="네":
           print("아즈렌-s 연고에 베타시토스테롤 항생제 추가\n1).수시로 환부에 도포한다.")
           s=input("도움이 더 필요하신가요? (네/아니오):")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break

       elif q2=="아니오":
           print("아즈렌-s\n1).수시로 환부에 도포한다.")
           s=input("도움이 더 필요하신가요? (네/아니오):")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break
       else:
           print("해당 증상에 맞는 약을 찾을 수 없습니다.전문가와 상담하세요.")
           s=input("도움이 더 필요하신가요? (네/아니오):")
           if s=="네":
               if s=="네":
                   continue
           else:
               print("프로그램을 종료합니다.")
               break
